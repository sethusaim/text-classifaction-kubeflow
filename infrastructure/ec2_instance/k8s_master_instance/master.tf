provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "k8s_master_instance" {
  ami                    = var.k8s_master_ami
  instance_type          = var.k8s_master_instance_type
  key_name               = var.k8s_master_key_pair_name
  vpc_security_group_ids = [aws_security_group.k8s_master_security_group.id]
  tags = {
    Name = var.tag_name
  }

  root_block_device {
    volume_size = var.k8s_master_volume_size
    volume_type = var.k8s_master_volume_type
    encrypted   = var.k8s_master_volume_encryption
  }

  connection {
    type    = "ssh"
    host    = self.public_ip
    user    = "ubuntu"
    timeout = "4m"
  }
}