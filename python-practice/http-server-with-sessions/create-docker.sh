#!/bin/bash

docker run --name node1 -v /home/ismdeep/code-practice/python-practice/http-server-with-sessions:/opt/honix -p 80:80 -it -d python:3.7 bash
