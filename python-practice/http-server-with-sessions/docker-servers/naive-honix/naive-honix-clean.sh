#!/bin/bash
for (( i = 0; i < 5; i++ )); do
	docker stop naive-honix-$i && docker rm naive-honix-$i
done
docker stop naive-honix-server && docker rm naive-honix-server
