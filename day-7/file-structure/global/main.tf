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

resource "aws_route53_zone" "primary" {
  name = "devopsdeployed.com"
}