#!/bin/sh 

python3 tools/download.py \
    --all \
    -v \
    --num-workers 32 \
    --failed-log /data/kinetics400/failed.txt
