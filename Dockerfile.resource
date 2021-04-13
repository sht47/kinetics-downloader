FROM alpine

RUN apk add -q --progress --update --no-cache curl tar 

WORKDIR /media
