import os
import platform
import subprocess
import sys

def get_cmd_output(cmd):
    return subprocess.check_output(cmd, shell=True).decode("utf-8")

os_info = platform.platform()
python_version = platform.python_version()
installed_packages = get_cmd_output(f"{sys.executable} -m pip freeze")
hardware_info = get_cmd_output('lshw -short')
ram_info = get_cmd_output('free -h')
graphics_info = get_cmd_output('lspci | grep VGA')
ubuntu_version = get_cmd_output('lsb_release -a')

with open("environment_info.txt", "w") as f:
    f.write(f"Operating System: {os_info}\n")
    f.write(f"\nPython Version: {python_version}\n")
    f.write("\nHardware Information:\n")
    f.write(hardware_info)
    f.write("\nRAM Information:\n")
    f.write(ram_info)
    f.write("\nGraphics Card Information:\n")
    f.write(graphics_info)
    f.write("\nUbuntu Version:\n")
    f.write(ubuntu_version)
    f.write("\nInstalled Packages:\n")
    f.write(installed_packages)
