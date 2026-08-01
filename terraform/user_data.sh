#!/bin/bash

yum update -y
yum install -y docker git
systemctl start docker
systemctl enable docker

# Pull the Docker image from Docker Hub
docker pull ${docker_hub_username}/python-app-2:${image_tag}
docker run -d -p 5000:5000 --restart unless-stopped ${docker_hub_username}/python-app-2:${image_tag}