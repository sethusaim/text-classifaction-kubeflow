resource "aws_eip" "elastic_ip" {
  vpc      = true
  instance = aws_instance.mlflow_instance.id
  tags = {
    Name = var.mlflow_eip_name
  }
}