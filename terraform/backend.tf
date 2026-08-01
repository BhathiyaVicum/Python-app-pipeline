# Store Terraform state remotely in S3

terraform {
  backend "s3" {
    bucket = "your-terraform-state-bucket-2024"
    key = "jenkins-pipeline/dev/terraform.tfstate"
    region = "us-east-1"
    encrypt = true
    use_lockfile = true
  }
}