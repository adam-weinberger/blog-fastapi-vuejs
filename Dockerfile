# pull official base image
FROM python:3.8.5

# set work directory
WORKDIR /home/app/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# install vim
RUN apt-get update
RUN apt-get install vim

# copy project
COPY src ./src