resource "aws_route_table" "ecom" {
  vpc_id = aws_vpc.ecom.id

  route {
    cidr_block = var.route_table_cidr_block
    gateway_id = aws_internet_gateway.ecom.id
  }
}

resource "aws_route_table_association" "ecom" {
  count = 2

  subnet_id      = aws_subnet.ecom.*.id[count.index]
  route_table_id = aws_route_table.ecom.id
}