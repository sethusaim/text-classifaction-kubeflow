terraform {
  backend "s3" {
    bucket = "ineuron-tf-state"
    key    = "tf_state"
    region = "us-east-1"
  }
}

module "k8s_master_instance" {
  source = "./ec2_instance/k8s_master_instance"
}

module "mlflow_instance" {
  source = "./ec2_instance/mlflow_instance"
}
module "eks_cluster" {
  source = "./eks_cluster"
}

module "artifacts_bucket" {
  source = "./s3_buckets/artifacts_bucket"
}

module "config_bucket" {
  source = "./s3_buckets/config_bucket"
}
module "jenkins_instance" {
  source = "./ec2_instance/jenkins_instance"
}

module "data_ingestion_ecr" {
  source = "./ecr_repo/data_ingestion_ecr"
}

module "data_transformation_ecr" {
  source = "./ecr_repo/data_transformation_ecr"
}

module "data_validation_ecr" {
  source = "./ecr_repo/data_validation_ecr"
}

module "model_training_ecr" {
  source = "./ecr_repo/model_training_ecr"
}

module "model_evaluation_ecr" {
  source = "./ecr_repo/model_evaluation_ecr"
}

module "model_pusher_ecr" {
  source = "./ecr_repo/model_pusher_ecr"
}
