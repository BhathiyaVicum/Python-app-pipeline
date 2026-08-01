# Store Terraform state remotely in S3

terraform {
  backend "s3" {
    bucket = "project-terraform-state-bhathiya"
    key = "dev/terraform.tfstate"
    region = "us-east-1"
    encrypt = true
    use_lockfile = true
  }
}