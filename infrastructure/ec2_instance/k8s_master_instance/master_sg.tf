resource "aws_security_group" "k8s_master_security_group" {
  name        = var.k8s_master_sg_group_name
  description = "Security Group for k8s_master Server"

  ingress {
    from_port   = var.k8s_master_ingress_from_port[0]
    to_port     = var.k8s_master_ingress_to_port[0]
    protocol    = var.k8s_master_protocol
    cidr_blocks = var.k8s_master_cidr_block
  }

  egress {
    from_port   = var.k8s_master_egress_from_port
    to_port     = var.k8s_master_egress_to_port
    protocol    = var.k8s_master_protocol
    cidr_blocks = var.k8s_master_cidr_block
  }

  tags = {
    Name = var.k8s_master_sg_group_name
  }
}