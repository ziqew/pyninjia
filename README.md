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