terraform {
    backend "s3" {
      bucket = "leefos3bucketforterraform"
      key = "leefopablo/workspace/terraform.tfstate"
      region = "us-east-1"
      dynamodb_table = "terraform-state-locking"
      encrypt = true
    }

  required_providers {
    aws = {
        source = "hashicrop/aws"
        version = "~>3.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

variable "db_pass" {
  description = "Password for the database table"
  sensitive = true
  type = string
}

locals {
  environment_name = "production"
}

module "web_app" {
  source = "../../../day-6/web-app-module"

  # Input Variables
  bucket_prefix    = "web-app-data-${local.environment_name}"
  domain           = "devopsdeployed.com"
  environment_name = local.environment_name
  instance_type    = "t2.micro"
  create_dns_zone  = false
  db_name          = "${local.environment_name}mydb"
  db_user          = "foo"
  db_pass          = var.db_pass
}