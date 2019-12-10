FROM docker.io/ubuntu:18.04
ENV JAVA_HOME /usr/local/jdk1.8.0_181
ENV PATH $PATH:$JAVA_HOME/bin
RUN apt-get update -y \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install wget tzdata net-tools telnet curl telnet inetutils-ping \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && apt-get clean && apt-get autoclean \
    && wget http://172.17.62.15:/jdk-8u181-linux-x64.tar.gz \
    && tar xf jdk-8u181-linux-x64.tar.gz -C /usr/local/ \
    && rm -rf jdk-8u181-linux-x64.tar.gz \
    && apt-get -y remove wget \
    && apt -y autoremove \
    && apt-get clean
