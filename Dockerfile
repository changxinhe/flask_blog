FROM python:3
RUN  apt-get install  default-libmysqlclient-dev -y && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
ADD requirements.txt requirements.txt
RUN pip install --upgrade pip  --index-url http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com && \
        pip install  -r requirements.txt --index-url http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

ADD . .

ENTRYPOINT ["python","main.py"]