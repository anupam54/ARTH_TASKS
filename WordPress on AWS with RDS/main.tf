#

resource "aws_instance" "WordPress_Server" {
    ami = "ami-0eeb03e72075b9bcc"
    instance_type = "t2.micro"
    associate_public_ip_address = true
    subnet_id = "subnet-017c9861ab204f3c0"
    vpc_security_group_ids = ["sg-0745b7b7e1e819742"]
    tags =  {
        Name = "WP_Instance_Terraform"
    }
}



resource "aws_db_subnet_group" "default_db_group" {
  name       = "main"
  subnet_ids = ["subnet-017c9861ab204f3c0","subnet-0e61bfbe6222dc041"]
  tags = {
    Name = "My DB subnet group"
  }
}



resource "aws_db_instance" "WordPress_DB" {
  allocated_storage    = 10
  engine               = "mysql"
  engine_version       = "5.7.31"
  instance_class       = "db.t2.micro"
  name                 = "mydb"
  username             = "myusername"
  password             = "mypassword"
  vpc_security_group_ids = ["sg-0745b7b7e1e819742"]
  publicly_accessible = true
  db_subnet_group_name = aws_db_subnet_group.default_db_group.name
}


