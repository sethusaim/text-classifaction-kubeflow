resource "aws_security_group" "ecom-cluster" {
  name        = var.ecom_sg_group_name
  description = "Cluster communication with worker nodes"
  vpc_id      = aws_vpc.ecom.id

  egress {
    from_port   = var.ecom_sg_group_egress_from_port
    to_port     = var.ecom_sg_group_egress_to_port
    protocol    = var.ecom_sg_group_protocol
    cidr_blocks = var.ecom_sg_group_cidr_block
  }

  tags = {
    Name = var.ecom_sg_group_tag_name
  }
}