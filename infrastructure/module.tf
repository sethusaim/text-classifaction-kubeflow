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

# module "ecom_kfp_policy" {
#   source = "./ecom_kfp_policy"
# }
