terraform {
  backend "s3" {
    bucket = "leefo-bucket-s3"
    key    = "path/to/my/key"
    region = "us-east-1"
    dynamodb_table = "terraform-state-locking"
    encrypt = true
  }

  required_providers {
    aws = {
        source = "hashicrop/aws"
        version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

locals {
  extra_tag = "extra-tag"
}

resource "aws_instance" "instance" {
  ami = var.ami
  instance_type = var.instance_type

  tags = {
    Name = var.instance_name
    Extra_tag = locals.extra_tag
  }
}

resource "aws_db_instance" "db_instance" {
    allocated_storage = 20
    storage_type = "gp2"
    engine = "postgres"
    engine_version = "12"
    instance_class = "db.t2.micro"
    name = "mydb"
    username = var.db_user
    password = var.db_pass
    skip_final_snapshot = true
}