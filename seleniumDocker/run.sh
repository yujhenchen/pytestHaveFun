#!/bin/bash

# get docker chrome image and run as container
docker pull selenium/standalone-chrome
docker run -d -p 4445:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome

# run tests using pytest
pytest testRemoteGoogle.py -s
