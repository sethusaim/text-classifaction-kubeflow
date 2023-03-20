variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "k8s_master_ami" {
  type    = string
  default = "ami-0c4f7023847b90238"
}

variable "k8s_master_instance_type" {
  type    = string
  default = "t2.micro"
}

variable "k8s_master_key_pair_name" {
  type    = string
  default = "sethusaim"
}

variable "tag_name" {
  type    = string
  default = "k8s_master Server"
}

variable "k8s_master_eip_name" {
  type    = string
  default = "k8s_master-ip"
}

variable "k8s_master_sg_group_name" {
  type    = string
  default = "k8s_master_sg_group"
}

variable "k8s_master_ingress_from_port" {
  type    = list(any)
  default = [22]
}

variable "k8s_master_cidr_block" {
  type    = list(any)
  default = ["0.0.0.0/0"]
}

variable "k8s_master_protocol" {
  type    = string
  default = "tcp"
}

variable "k8s_master_ingress_to_port" {
  type    = list(any)
  default = [22]
}

variable "k8s_master_egress_from_port" {
  type    = number
  default = 0
}

variable "k8s_master_egress_to_port" {
  type    = number
  default = 65535
}

variable "k8s_master_volume_size" {
  default = 50
  type    = number
}

variable "k8s_master_volume_type" {
  default = "gp2"
  type    = string
}

variable "k8s_master_volume_encryption" {
  default = true
  type    = bool
}
