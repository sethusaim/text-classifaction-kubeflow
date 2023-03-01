variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "feature_store_bucket_name" {
  type    = string
  default = "ecom-config"
}

variable "aws_account_id" {
  type    = string
  default = "566373416292"
}

variable "force_destroy_bucket" {
  type    = bool
  default = true
}