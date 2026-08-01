variable "region" {
    description = "The AWS region to deploy resources"
    type        = string
    default     = "us-east-1"
}

variable "docker_hub_username" {
  description = "Docker Hub username"
  type        = string
}

variable "image_tag" {
  description = "Docker image tag"
  type        = string
  default     = "latest"
}