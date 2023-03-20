resource "aws_eip" "elastic_ip" {
  vpc      = true
  instance = aws_instance.k8s_master_instance.id
  tags = {
    Name = var.k8s_master_eip_name
  }
}