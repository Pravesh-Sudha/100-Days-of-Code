variable "instance_name" {
  type = string
  description = "Name of EC2 Instance"  
}

variable "ami" {
  description = "Ami of EC2"
  type = string
  default = "ami-053b0d53c279acc90"
}
variable "instance_type" {
  description = "Type of EC2 instance"
  default = "t2.micro"
  type = string
}
variable "db_user" {
  description = "username for database"
  default = "Foo"
  type = string
}
variable "db_pass" {
  description = "password for database"
  default = "foo123"
  sesensitive = true
}
