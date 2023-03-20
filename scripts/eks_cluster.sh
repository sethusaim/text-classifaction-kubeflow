#!bin/bash

eksctl create cluster --name tekton --version 1.22 --region us-east-1 --zones us-east-1a,us-east-1b --nodegroup-name tekton-nodes --node-type t2.large --nodes-min 2 --nodes-max 4 --with-oidc