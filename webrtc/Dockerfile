FROM python:3.9
USER root

RUN apt-get update
RUN apt-get -y install locales locales-all && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

COPY requirements.txt /root/

RUN apt-get install -y vim less iputils-ping curl iproute2 traceroute
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
EXPOSE 5000
EXPOSE 6000
RUN pip install -r /root/requirements.txt
