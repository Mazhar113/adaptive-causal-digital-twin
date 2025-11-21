
module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = var.cluster_name
  cluster_version = "1.27"
  subnets         = [aws_subnet.twin_subnet.id]
  vpc_id          = aws_vpc.twin_vpc.id
  node_groups = {
    default = {
      desired_capacity = 1
      max_capacity     = 2
      min_capacity     = 1
      instance_type    = "t3.medium"
    }
  }
}
