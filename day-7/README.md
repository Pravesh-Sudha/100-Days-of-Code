# Day 7 of 100DaysofCode

Feeling excited to start Day 7 of 100 DaysOfCode, today, I learnt about different kinds of environment in terraform and workspaces like Staging Environment, Development Environment and Production Environment.

- Note about using separate AWS accounts (avoids prefix issues, improved IAM control)
  - Cover this in advanced section?
  
```
provider “aws” {
  region = “us-east-1”
  assume_role {
    role_arn = “arn:aws:iam::123456789012:role/iac”
  }
}
```

Warning about manually switching environments
```
terraform workspace new production
terraform workspace list
terraform workspace select staging
```


