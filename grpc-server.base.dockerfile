FROM golang:1.17.5-buster

RUN apt update;\
    apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev;\
    cd /opt;\
    wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz;\
    tar xzf Python-3.9.0.tgz;\
    cd Python-3.9.0;\
    ./configure --enable-optimizations;\
    make altinstall;\
    ln -s /usr/local/bin/python3.9 /usr/local/bin/python3;\
    ln -s /usr/local/bin/pip3.9 /usr/local/bin/pip3;

COPY ../helloworld /usr/local/go/src

WORKDIR /usr/local/go/src/greeter_client_py

RUN pip3 install -r requirements.txt

WORKDIR /usr/local/go/src/greeter_client_go

ENV HTTP_PROXY="http://192.168.0.135:4080"
ENV HTTPS_PROXY="http://192.168.0.135:4080"

RUN go mod tidy

ENV HTTP_PROXY=
ENV HTTPS_PROXY=

RUN nohup go run .




