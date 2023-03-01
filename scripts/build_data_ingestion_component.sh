#!bin/bash

mongodb_url=$1

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 566373416292.dkr.ecr.us-east-1.amazonaws.com

docker build --build-arg MONGODB_URL=$mongodb_url -t 566373416292.dkr.ecr.us-east-1.amazonaws.com/ecom_data_ingestion:latest ecom/data_ingestion/

docker push 566373416292.dkr.ecr.us-east-1.amazonaws.com/ecom_data_ingestion:latest
