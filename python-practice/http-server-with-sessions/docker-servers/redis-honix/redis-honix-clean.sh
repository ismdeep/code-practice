#!/bin/bash
for (( i = 0; i < 5; i++ )); do
	docker stop redis-honix-$i && docker rm redis-honix-$i
done
docker stop redis-honix-server && docker rm redis-honix-server
