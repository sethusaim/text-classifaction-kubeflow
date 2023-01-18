terraform {
  backend "s3" {
    bucket = "ecom-ineuron-tf-state"
    key    = "tf_state"
    region = "ap-south-1"
  }
}

module "ecom_feature_store" {
  source = "./ecom_feature_store"
}

module "ecom_artifacts" {
  source = "./ecom_artifacts"
}