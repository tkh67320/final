#!/bin/bash
source /home/student/projects/final/bin/activate
screen uwsgi --socket 127.0.0.1:4305 \
--venv /home/student/projects/final \
--wsgi-file /home/student/projects/final/final/wsgi.py \
--master
