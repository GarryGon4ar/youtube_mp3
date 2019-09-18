FROM python:3.6
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /youtubedl
WORKDIR /youtubedl
RUN pip install pip -U
ADD requirements.txt /youtubedl/
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev  -y
ADD . /youtubedl/

