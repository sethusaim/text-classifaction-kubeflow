#!bin/bash

eksctl create cluster --name kubeflow --version 1.22 --region us-east-1 --zones us-east-1a,us-east-1b --nodegroup-name kubeflow-nodes --node-type t2.medium --nodes 5 --nodes-min 5 --nodes-max 6 --with-oidc