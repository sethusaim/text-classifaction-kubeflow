#!bin/bash

path=$1

repo=$2

build_number=$3

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 566373416292.dkr.ecr.us-east-1.amazonaws.com

docker build -t 566373416292.dkr.ecr.us-east-1.amazonaws.com/$repo:$build_number $path/

docker push 566373416292.dkr.ecr.us-east-1.amazonaws.com/$repo:$build_number