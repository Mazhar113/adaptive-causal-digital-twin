
resource "aws_db_instance" "twin_db" {
  allocated_storage    = 20
  engine               = "postgres"
  instance_class       = "db.t3.micro"
  name                 = "twin_db"
  username             = "twin"
  password             = var.db_password
  skip_final_snapshot  = true
  publicly_accessible  = false
}
