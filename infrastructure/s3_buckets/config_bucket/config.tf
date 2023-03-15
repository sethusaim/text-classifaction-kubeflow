resource "random_integer" "random" {
  min = 1
  max = 50000
}

resource "aws_s3_bucket" "config_bucket" {
  bucket        = "${random_integer.random.id}${var.config_bucket_name}"
  force_destroy = var.force_destroy_bucket
}