FROM python:3.7

MAINTAINER ismdeep@protonmail.com

# COPY -r -v /data/code-practice/python-practice/http-server-with-sessions /opt/honix

RUN mkdir /root/.pip
COPY ./pip.conf /root/.pip
COPY ./honix /opt/honix
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

RUN pip install ismdeep-utils

EXPOSE 80

ENTRYPOINT ["/docker-entrypoint.sh"]