#!bin/bash

docker build -t 566373416292.dkr.ecr.us-east-1.amazonaws.com/kubeflow-testing:latest .
          
docker push 566373416292.dkr.ecr.us-east-1.amazonaws.com/kubeflow-testing:latest