terraform {
  backend "s3" {
    bucket = "ineuron-tf-state"
    key    = "tf_state"
    region = "us-east-1"
  }
}

module "ecom_artifacts" {
  source = "./ecom_artifacts"
}

module "ecom_config" {
  source = "./ecom_config"
}

module "ecom_model_registry" {
  source = "./ecom_model_registry"
}
