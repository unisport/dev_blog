FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    build-essential \
    ca-certificates \
    python-setuptools \
    python-dev

RUN easy_install pip
RUN pip install -U pip
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD . /mnt

WORKDIR /mnt

CMD make serve-global
