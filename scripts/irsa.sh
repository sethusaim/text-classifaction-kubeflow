#!bin/bash

# arn:aws:iam::347460842118:policy/ecom_tekton_policy - Create this policy with s3 and ecr full access

eksctl create iamserviceaccount --name kube-ecom-sa --cluster ecom-tekton --namespace ecom --role-name kube_ecom_role --attach-policy-arn=arn:aws:iam::347460842118:policy/ecom_tekton_policy --approve --override-existing-serviceaccounts

kubectl create clusterrolebinding kube-ecom-sa-cluster-role-binding --clusterrole=admin --serviceaccount=ecom:kube-ecom-sa
