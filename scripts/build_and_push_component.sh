#!bin/bash

path=$1

repo=$2

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 566373416292.dkr.ecr.us-east-1.amazonaws.com

docker build -t 566373416292.dkr.ecr.us-east-1.amazonaws.com/ecom_model_training:latest $path/

docker push 566373416292.dkr.ecr.us-east-1.amazonaws.com/$repo:latest