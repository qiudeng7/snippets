# 一个收集系统占用的脚本
下面是一个使用示例。

```bash
# centos7 yum换源
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

# yum安装依赖
yum install python3 gcc python3-devel
# 使用虚拟环境
python -m venv venv
source venv/bin/activate

# pip安装依赖
pip install psutil -i https://pypi.tuna.tsinghua.edu.cn/simple

# 运行脚本
python system_usage.py

```

也可以使用sample.service创建一个systemd服务，让它自动运行。