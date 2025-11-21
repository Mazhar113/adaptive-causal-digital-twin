
variable "aws_region" {
  default = "us-east-1"
}
variable "cluster_name" {
  default = "digital-twin-eks"
}
variable "db_password" {
  type = string
  default = "twinpass"
}
