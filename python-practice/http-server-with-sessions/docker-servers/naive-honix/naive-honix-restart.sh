#!/bin/bash
for (( i = 0; i < 5; i++ )); do
	docker restart naive-honix-$i
done
docker restart naive-honix-server
