FROM python:3.7-alpine AS base
LABEL maintainer="German Martinez"
RUN apk add build-base postgresql-dev bash nano

FROM base
COPY . /black-forest
WORKDIR /black-forest
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

ENTRYPOINT [ "/black-forest/run-prod-server.sh" ]