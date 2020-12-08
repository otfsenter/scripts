touch ~/.pypirc

```
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username =
password =
```

* 在setup.py目录终端执行命令, 安装setuptools和wheel

python3 -m pip install --upgrade setuptools wheel


* 在setup.py目录终端执行命令, 会在setup.py同一级目录下生成dist文件夹，里面有两个文件，一个***.tar.gz，一个****.whl文件

python3 setup.py sdist bdist_wheel


* 在setup.py目录终端执行命令，安装twine

python3 -m pip install --upgrade twine

* 在setup.py目录终端执行命令，就上传了自己的python库。

python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

登陆pypi官网，查看自己的项目即可看到上传的python库。
