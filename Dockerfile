FROM alpine

RUN apk add -q --progress --update --no-cache ffmpeg python3 py3-pip gzip
RUN pip install --upgrade pip
RUN pip install youtube_dl

COPY ./youtube-dl.conf /etc/youtube-dl.conf

WORKDIR /media
