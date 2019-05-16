#!/bin/bash
for (( i = 0; i < 5; i++ )); do
	docker restart redis-honix-$i
done
docker restart redis-honix-server
