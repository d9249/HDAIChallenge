# nohup python -u train_preliminary.py &
# tail -f nohup.out

import pandas as pd
import numpy as np
import bisect
from tqdm import tqdm
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from supervised.automl import AutoML

train = pd.read_csv('./data/train.csv').drop(columns=['SAMPLE_ID'])
test = pd.read_csv('./data/test.csv').drop(columns=['SAMPLE_ID'])
train['ATA'] = pd.to_datetime(train['ATA'])
test['ATA'] = pd.to_datetime(test['ATA'])

for df in [train, test]:
    df['year'] = df['ATA'].dt.year
    df['month'] = df['ATA'].dt.month
    df['day'] = df['ATA'].dt.day
    df['hour'] = df['ATA'].dt.hour
    df['minute'] = df['ATA'].dt.minute
    df['weekday'] = df['ATA'].dt.weekday

train.drop(columns='ATA', inplace=True)
test.drop(columns='ATA', inplace=True)
categorical_features = ['ARI_CO', 'ARI_PO', 'SHIP_TYPE_CATEGORY', 'ID', 'SHIPMANAGER', 'FLAG']
encoders = {}

for feature in tqdm(categorical_features, desc="Encoding features"):
    le = LabelEncoder()
    train[feature] = le.fit_transform(train[feature].astype(str))
    le_classes_set = set(le.classes_)
    test[feature] = test[feature].map(lambda s: '-1' if s not in le_classes_set else s)
    le_classes = le.classes_.tolist()
    bisect.insort_left(le_classes, '-1')
    le.classes_ = np.array(le_classes)
    test[feature] = le.transform(test[feature].astype(str))
    encoders[feature] = le

train.fillna(train.mean(), inplace=True)
test.fillna(train.mean(), inplace=True)

def get_season(month):
    if month in [3, 4, 5]:
        return 2
    elif month in [6, 7, 8]:
        return 3
    elif month in [9, 10, 11]:
        return 4
    else:
        return 1

def get_time_of_day(hour):
    if 5 <= hour < 12:
        return 1
    elif 12 <= hour < 17:
        return 2
    elif 17 <= hour < 21:
        return 3
    else:
        return 4

train['WIND_INTENSITY'] = np.sqrt(train['U_WIND']**2 + train['V_WIND']**2)
test['WIND_INTENSITY'] = np.sqrt(test['U_WIND']**2 + test['V_WIND']**2)
train['U_WIND_SQUARE'] = train['U_WIND'] ** 2
test['U_WIND_SQUARE'] = test['U_WIND'] ** 2
train['V_WIND_SQUARE'] = train['V_WIND'] ** 2
test['V_WIND_SQUARE'] = test['V_WIND'] ** 2
train['SEASON'] = train['month'].apply(get_season)
test['SEASON'] = test['month'].apply(get_season)
train['WEEKEND'] = train['weekday'].apply(lambda x: 1 if x >= 5 else 0)
test['WEEKEND'] = test['weekday'].apply(lambda x: 1 if x >= 5 else 0)
train['VOLUME'] = train['BREADTH'] * train['LENGTH'] * train['DEPTH']
test['VOLUME'] = test['BREADTH'] * test['LENGTH'] * test['DEPTH']
train['WIND_DIRECTION'] = np.arctan2(train['V_WIND'], train['U_WIND']) * (180/np.pi)
test['WIND_DIRECTION'] = np.arctan2(test['V_WIND'], test['U_WIND']) * (180/np.pi)
train['WIND_DIRECTION'] = train['WIND_DIRECTION'].apply(lambda x: x+360 if x < 0 else x)
test['WIND_DIRECTION'] = test['WIND_DIRECTION'].apply(lambda x: x+360 if x < 0 else x)
train['WIND_SPEED_DIR'] = train['WIND_INTENSITY'] * train['WIND_DIRECTION']
test['WIND_SPEED_DIR'] = test['WIND_INTENSITY'] * test['WIND_DIRECTION']

X_train = train.drop(columns='CI_HOUR')
Y_train = train['CI_HOUR']

scaler = MinMaxScaler()
train_scaled = scaler.fit_transform(X_train)
test_scaled = scaler.transform(test)

X_train = pd.DataFrame(train_scaled, columns = X_train.columns)
test = pd.DataFrame(test_scaled, columns = test.columns)

automl = AutoML(
    algorithms=["CatBoost", "Xgboost", "LightGBM", "Random Forest"],
    mode="Compete",
    ml_task="regression",
    eval_metric='mae',
    random_state=42,
    total_time_limit=None,
    model_time_limit=None
)

automl.fit(X_train, Y_train)
pred = automl.predict(test)
submit = pd.read_csv('./data/sample_submission.csv')
submit['CI_HOUR'] = pred
submit.to_csv('./csv/submit.csv', index=False)