#!/bin/bash
docker run --name redis-db -d redis

for (( i = 0; i < 5; i++ )); do
	docker run --name redis-honix-$i --link redis-db:redis:db -d redis-honix
done

docker run --name redis-honix-server -v /data/code-practice/python-practice/http-server-with-sessions/docker-servers/redis-honix/nginx/conf.d:/etc/nginx/conf.d \
--link redis-honix-0:redis-honix-0 \
--link redis-honix-1:redis-honix-1 \
--link redis-honix-2:redis-honix-2 \
--link redis-honix-3:redis-honix-3 \
--link redis-honix-4:redis-honix-4 \
-p 80:80 -d nginx