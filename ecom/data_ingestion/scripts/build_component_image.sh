#!bin/bash

docker build -t 566373416292.dkr.ecr.us-east-1.amazonaws.com/ecom-data-ingestion:latest .
          
docker push 566373416292.dkr.ecr.us-east-1.amazonaws.com/ecom-data-ingestion:latest