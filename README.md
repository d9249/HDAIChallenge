# [HD 현대 AI Challenge](https://dacon.io/competitions/official/236158/overview/description>)

![image](https://github.com/d9249/HDAIChallenge/blob/main/image/HD.png)

최근 건설 현장 운용 효율화를 위하여 건설 현장의 디지털화와 건설 장비 Fleet Management 솔루션의 필요성이 대두되고 있습니다. 

장비 운용의 효율성은 해당 작업에 최적화된 장비 조합을 찾는 것에서 시작합니다. 최적화된 장비 조합을 찾기 위해서는 장비의 작업량을 정확하게 예측하고, 이 결과가 실시간으로 모니터링 되어야 합니다.이에 건설 장비로부터 취득된 데이터를 이용하여, 작업 중량을 예측하는 AI 알고리즘 개발을 제안합니다.

## 건설기계 센서데이터를 활용한 작업 중량 예측 모델 개발

작업자의 운전 성향과 숙련도에 영향을 받지 않고 정확한 작업 중량을 예측할 수 있는 모델을 개발해야 합니다.

건설기계에 부착된 센서 데이터를 활용하여 중량을 예측해야 합니다.

제공되는 데이터에서 각각의 파일은 한 개의 Label값을 가지고 있으며 작업자와 중량 외의 조건은 모두 동일하다고 가정합니다. (예 – 건설기계, 작업 동작, 데이터 수집 장소 등)

[채용 특전]본선 수상자 채용 지원시 서류전형면제, 본선 진출자 채용 지원시 가산점

> 예선 학습 코드는 `train_preliminary.py`이며, 예선에서 학습된 `weight`와 `model`은 `AutoML_1`에 저장되어있으며, 학습 과정에 대한 결과와 리포트 또한 작성되어 있습니다. 또한 `prediction_preliminary.py`을 실행하면 예선 결과(score: 31.81379)에 대한 예측 복원이 가능합니다.
> 
> 본선 학습 코드는 `train_final.ipynb`이며, 본선에서 학습된 `weight`는 `weight(final)`폴더에 저장되어있으며, 학습 과정을 포함하고 있습니다. 또한 실험 재현을 위해서 `prediction_reproducibility_final.ipynb`을 작성해두었으며, 해당 코드를 통해 본선 예측 결과(score: 98.21432)의 복원이 가능합니다.
> 
> 학습 환경은 Docker를 통해 보관해두었기에, [Docker hub 링크](https://hub.docker.com/repository/docker/dodo9249/hdaichallenge/general)를 따라 pull하면, 제가 학습한 환경을 바로 사용할 수 있습니니다. 예선(version:1.0)과 본선(version:2.0) 동일한 환경에서 실험을 수행하였습니다.

## 예선 결과

![image](https://github.com/d9249/HDAIChallenge/blob/main/leaderboard(preliminary)/private.JPG)

![image](./leaderboard(final)/final.JPG)

## 본선 결과

![image](./leaderboard(final)/final_leardboard.JPG)

## 실험 환경

> environment_info.txt

```
CPU: 12th Gen Intel(R) Core(TM) i9-12900K

RAM: SAMSUNG DDR4 128GB

GPU: Nvidia RTX3090 24GB

Operating System: Linux-5.15.0-83-generic-x86_64-with-debian-buster-sid
Ubuntu Version:
Distributor ID: Ubuntu
Description: Ubuntu 18.04.6 LTS
Release: 18.04
Codename: bionic

Python Version: 3.7.13
```

## 설치된 패키지

> requirements.txt

```
alembic==1.12.0
anyio==3.7.1
backcall==0.2.0
brotlipy==0.7.0
catboost==1.2.2
category-encoders==2.6.2
certifi==2021.10.8
cffi==1.15.0
charset-normalizer==2.0.4
cloudpickle==2.2.1
colorama==0.4.4
colorlog==6.7.0
colour==0.1.5
conda==4.12.0
conda-content-trust==0+unknown
conda-package-handling==1.8.1
cryptography==36.0.0
cycler==0.11.0
decorator==5.1.1
dtreeviz==2.2.2
exceptiongroup==1.1.3
fonttools==4.38.0
graphviz==0.20.1
greenlet==3.0.0
h11==0.14.0
httpcore==0.17.3
httpx==0.24.1
idna==3.3
importlib-metadata==6.7.0
importlib-resources==5.12.0
iniconfig==2.0.0
ipython==7.34.0
jedi==0.19.1
joblib==1.3.2
kiwisolver==1.4.5
lightgbm==4.1.0
llvmlite==0.39.1
Mako==1.2.4
Markdown==3.4.4
MarkupSafe==2.1.3
matplotlib==3.5.3
matplotlib-inline==0.1.6
mljar-supervised==1.0.2
numba==0.56.4
numpy==1.21.6
optuna==3.4.0
packaging==23.2
pandas==1.3.5
parso==0.8.3
patsy==0.5.3
pexpect==4.8.0
pickleshare==0.7.5
Pillow==9.5.0
pip==21.2.2
plotly==5.17.0
pluggy==1.2.0
prompt-toolkit==3.0.39
ptyprocess==0.7.0
pycosat==0.6.3
pycparser==2.21
Pygments==2.16.1
pyOpenSSL==22.0.0
pyparsing==3.1.1
PySocks==1.7.1
pytest==7.4.2
python-dateutil==2.8.2
python-telegram-bot==20.3
pytz==2023.3.post1
PyYAML==6.0.1
requests==2.27.1
ruamel-yaml-conda==0.15.100
scikit-learn==1.0.2
scikit-plot==0.3.7
scipy==1.7.3
seaborn==0.12.2
setuptools==61.2.0
shap==0.42.1
six==1.16.0
slicer==0.0.7
sniffio==1.3.0
SQLAlchemy==2.0.22
statsmodels==0.13.5
tabulate==0.9.0
tenacity==8.2.3
threadpoolctl==3.1.0
tomli==2.0.1
tqdm==4.63.0
traitlets==5.9.0
typing_extensions==4.7.1
urllib3==1.26.8
wcwidth==0.2.8
wheel==0.37.1
wordcloud==1.9.2
xgboost==1.6.2
zipp==3.15.0
```
