#!/bin/bash
for (( i = 0; i < 5; i++ )); do
	docker run --name naive-honix-$i -d naive-honix
done

docker run --name naive-honix-server -v /data/code-practice/python-practice/http-server-with-sessions/docker-servers/naive-honix/nginx/conf.d:/etc/nginx/conf.d \
--link naive-honix-0:naive-honix-0 \
--link naive-honix-1:naive-honix-1 \
--link naive-honix-2:naive-honix-2 \
--link naive-honix-3:naive-honix-3 \
--link naive-honix-4:naive-honix-4 \
-p 80:80 -d nginx