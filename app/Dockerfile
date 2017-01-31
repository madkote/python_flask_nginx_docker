FROM ubuntu:latest
MAINTAINER madkote "madkote@bluewin.ch"

# install tools
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev
RUN apt-get install -y python3 python3-pip python3-dev

# update python pip
RUN pip install --upgrade pip
RUN pip3 install --upgrade pip

# get app sources
COPY . /app

# install app requirements
WORKDIR /app
RUN pip3 install -r requirements.txt

# expose port
EXPOSE  5000

# run
CMD ["python3", "main.py"]
