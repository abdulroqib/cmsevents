# pull official base image
FROM python:3.8.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    build-base zlib libjpeg-turbo-dev libpng-dev \
    freetype-dev lcms2-dev libwebp-dev \
    harfbuzz-dev fribidi-dev tcl-dev tk-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "./entrypoint.sh"]