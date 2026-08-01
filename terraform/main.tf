# Security Group - Allow web traffic
resource "aws_security_group" "web_sg" {
  name_prefix = "jenkins-demo-sg"

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instance
resource "aws_instance" "web_server" {
  ami           = "ami-02b64aa047cb5edf5"
  instance_type = "t3.micro"
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  user_data = templatefile("${path.module}/user_data.sh", {
    docker_hub_username = var.docker_hub_username
    image_tag           = var.image_tag
  })

  tags = {
    Name = "Jenkins-Demo-App"
  }
}