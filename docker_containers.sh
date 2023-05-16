#!/bin/bash
export ROOT="/var/grafana"
export DATA_DIR="$ROOT/data"
sudo mkdir -p $ROOT $DATA_DIR

docker run -d \
	--name metal-data-postgres \
    -e POSTGRES_USER=metal \
	-e POSTGRES_PASSWORD=test \
    -e POSTGRES_DB=metal_db \
    -v /var/postgres_container_data/metal_data:/var/lib/postgresql/data \
    -p 5430:5432 \
	postgres:12

docker run -d \
	--name grafana-data-postgres \
    -e POSTGRES_USER=metal_user \
	-e POSTGRES_PASSWORD=test \
    -e POSTGRES_DB=metal \
    -v /var/postgres_container_data/metal_grafana_postgres:/var/lib/postgresql/data \
    -p 5431:5432 \
	postgres:12

echo "Waiting for pg Containers"
sleep 10
sudo chown -R 472:472 $ROOT
docker run -d --name=grafanna_test -v /var/grafana/data:/var/lib/grafana -v /var/grafana/grafana.ini:/etc/grafana/grafana.ini -p 3001:3000 grafana/grafana
