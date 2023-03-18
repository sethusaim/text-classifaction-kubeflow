resource "aws_vpc" "ecom" {
  cidr_block = var.cluster_vpc_cidr_block

  tags = tomap({
    "Name"                                      = var.cluster_vpc_tag_name,
    "kubernetes.io/cluster/${var.cluster-name}" = "shared",
  })
}

resource "aws_subnet" "ecom" {
  count = 2

  availability_zone       = data.aws_availability_zones.available.names[count.index]
  cidr_block              = "10.0.${count.index}.0/24"
  map_public_ip_on_launch = true
  vpc_id                  = aws_vpc.ecom.id

  tags = tomap({
    "Name"                                      = var.cluster_subnet_tag_name
    "kubernetes.io/cluster/${var.cluster-name}" = "shared",
  })
}


resource "aws_internet_gateway" "ecom" {
  vpc_id = aws_vpc.ecom.id

  tags = {
    Name = var.cluster_internet_gateway_tag_name
  }
}