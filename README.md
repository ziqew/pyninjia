# pyninjia
py app


## pyenv
https://gitee.com/ziqew/pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
git clone https://gitee.com/ziqew/pyenv.git ~/.pyenv

https://gitee.com/ziqew/pyenv-virtualenv.git

git clone https://gitee.com/ziqew/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv


pyenv virtualenv 3.10.9 devops_py

使用.python-version
pyenv versions
echo 'env_raaynk_hello_world' >> .python-version

手动激活
pyenv activate devops_py
pyenv deactivate

~/.pyenv/shims/python
~/.pyenv/shims/python3
$(pyenv root)/versions/<selected version>/bin

python 华为镜像
https://repo.huaweicloud.com/python/3.10.9/
wget https://repo.huaweicloud.com/python/3.10.9/Python-3.10.9.tar.xz ~/.pyenv/cache/

pip
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip config set install.trusted-host mirrors.aliyun.com

python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
python3 -m pip config set install.trusted-host mirrors.aliyun.com


anaconda 安装目录
C:\Users\gongw\anaconda3

conda install SSL 问题
CondaSSLError: OpenSSL appears to be unavailable on this machine.
复制 C:\Users\gongw\anaconda3\Library\bin libcrypto-1_1-x64.dll libssl-1_1-x64.dll

到 C:\Users\gongw\anaconda3\DLLs





conda info -e



conda --v


conda env list


conda env -h


创建环境

conda create -n py-dl-env python=3.9

conda create -n py-torch-env python=3.9

激活环境

source activate py-dl-env

conda activate py-dl-env

conda activate py-torch-env

安装 pytorch with cuda
检查 cuda
nvidia-smi
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.7 -c pytorch -c nvidia

切换环境
conda deactivate

移除环境
conda env remove -n


conda list -e > requirements.txt

pip install -r requirements.txt

python 安装包的路径
python -m site 
(py-dl-env) PS D:\dev\pyninjia> python -m site
sys.path = [
    'D:\\dev\\pyninjia',
    'C:\\Users\\gongw\\anaconda3\\envs\\py-dl-env\\python39.zip',
    'C:\\Users\\gongw\\anaconda3\\envs\\py-dl-env\\DLLs',
    'C:\\Users\\gongw\\anaconda3\\envs\\py-dl-env\\lib',
    'C:\\Users\\gongw\\anaconda3\\envs\\py-dl-env',
    'C:\\Users\\gongw\\anaconda3\\envs\\py-dl-env\\lib\\site-packages',
]
USER_BASE: 'C:\\Users\\gongw\\AppData\\Roaming\\Python' (doesn't exist)
USER_SITE: 'C:\\Users\\gongw\\AppData\\Roaming\\Python\\Python39\\site-packages' (doesn't exist)
ENABLE_USER_SITE: True

pip aliyun mirror
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip config set install.trusted-host mirrors.aliyun.com

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm
