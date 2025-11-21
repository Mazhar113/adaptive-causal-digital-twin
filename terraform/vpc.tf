
data "aws_availability_zones" "available" {}
resource "aws_vpc" "twin_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = { Name = "twin-vpc" }
}
resource "aws_subnet" "twin_subnet" {
  vpc_id            = aws_vpc.twin_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = data.aws_availability_zones.available.names[0]
  tags = { Name = "twin-subnet" }
}
