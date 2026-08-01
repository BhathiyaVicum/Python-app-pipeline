# 🚀 CI/CD Pipeline with Jenkins, Terraform, Docker & AWS

[![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-blue?style=for-the-badge&logo=jenkins)](https://www.jenkins.io/)
[![Terraform](https://img.shields.io/badge/Terraform-Infrastructure%20as%20Code-purple?style=for-the-badge&logo=terraform)](https://www.terraform.io/)
[![Docker](https://img.shields.io/badge/Docker-Containerization-blue?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-orange?style=for-the-badge&logo=amazonaws)](https://aws.amazon.com/free/)

## 📖 Overview

This project demonstrates a **fully automated CI/CD pipeline** that builds and deploys a Python Flask application to AWS EC2. The entire infrastructure is provisioned using **Infrastructure as Code (IaC)** with Terraform, containerized with Docker, and orchestrated by Jenkins.

### 🎯 Key Features

- ✅ **Automated Pipeline** – Jenkins orchestrates the entire CI/CD workflow
- ✅ **Continuous Integration** – Code is built and containerized on every build
- ✅ **Continuous Deployment** – Application is deployed to AWS EC2
- ✅ **GitOps** – Everything is defined in code (Infrastructure as Code)
- ✅ **Free Tier** – All AWS resources within free tier limits

## 🛠️ Technology Stack

| Category | Technology |
|:---|:---|
| **CI/CD** | Jenkins |
| **Infrastructure as Code** | Terraform |
| **Containerization** | Docker |
| **Container Registry** | Docker Hub |
| **Cloud Provider** | AWS EC2 |
| **Application** | Python Flask |
| **Version Control** | GitHub |

## 📸 Screenshots

<img width="1918" height="1012" alt="Jenkins Pipeline" src="https://github.com/user-attachments/assets/d66de0c5-a4ab-453d-a55d-8c1dc32d915d" />

<img width="1918" height="1017" alt="Terraform Apply" src="https://github.com/user-attachments/assets/e9d2df0c-c5fe-4ab0-bf7b-eea88fa85458" />

<img width="1918" height="1022" alt="Live Application" src="https://github.com/user-attachments/assets/c7aaf243-c08b-43eb-9fab-5376fe8914a6" />

## 📁 Project Structure

```
python-app-pipeline/
│
├── app/
│   ├── app.py              # Flask web application
│   └── requirements.txt    # Python dependencies
│
├── terraform/
│   ├── main.tf             # AWS infrastructure
│   ├── variables.tf        # Input variables
│   ├── outputs.tf          # Output values
│   └── user_data.sh        # EC2 startup script
│
├── Dockerfile              # Docker container instructions
├── Jenkinsfile             # Jenkins pipeline definition
└── README.md               # Project documentation
```

## 📋 Pipeline Stages

| Stage | Description | Tools Used |
|:---|:---|:---|
| **Git Clone** | Pulls the latest code from GitHub | Git |
| **Build Docker Image** | Creates a Docker container image of the Flask app | Docker |
| **Push Docker Hub** | Uploads the image to Docker Hub repository | Docker CLI |
| **Terraform Deploy** | Provisions AWS EC2 instance and Security Groups | Terraform |
| **Get URL** | Retrieves the EC2 public IP address | Terraform Output |

### Pipeline Flow

```
Jenkins Build (Manual) → Git Clone → Build Docker Image → Push Docker Hub → Terraform Apply → EC2 Running → App Live
```

## 🚀 Getting Started

### Prerequisites

| Tool | Purpose | Installation Link |
|:---|:---|:---|
| **Java 11+** | Required for Jenkins | [Adoptium](https://adoptium.net/) |
| **Jenkins** | CI/CD server | [Jenkins Download](https://www.jenkins.io/download/) |
| **Docker** | Containerization | [Docker Desktop](https://www.docker.com/products/docker-desktop/) |
| **Terraform** | Infrastructure as Code | [Terraform Download](https://www.terraform.io/downloads) |
| **AWS CLI** | AWS interaction | [AWS CLI Install](https://aws.amazon.com/cli/) |
| **Git** | Version control | [Git Download](https://git-scm.com/downloads) |

### AWS Account Setup

**1. Create an IAM User**
- Go to AWS Console → IAM → Users → Create user
- Username: `jenkins-user`
- Attach policies: `AmazonEC2FullAccess`, `IAMFullAccess`

**2. Generate Access Keys**
- Click on the user → Security credentials → Create access key
- Copy and save:
  - `Access Key ID`
  - `Secret Access Key`
- ⚠️ **Never share these keys publicly!**

**3. Create a Key Pair (Optional for SSH)**
- EC2 → Key Pairs → Create key pair
- Download the `.pem` file for SSH access

### Local Environment Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/BhathiyaVicum/python-app-pipeline.git
cd python-app-pipeline
```

#### 2. Start Jenkins Locally

```bash
# Download Jenkins WAR file
curl -O https://get.jenkins.io/war-stable/latest/jenkins.war

# Run Jenkins
java -jar jenkins.war --httpPort=8080
```

**Access Jenkins:** `http://localhost:8080`

#### 3. Configure Jenkins Credentials

**Add Docker Hub Credentials:**
- **Kind:** `Username with password`
- **Username:** Your Docker Hub username
- **Password:** Your Docker Hub password
- **ID:** `dockerhub-creds`

**Add AWS Credentials:**
- **Kind:** `AWS Credentials`
- **Access Key ID:** Your AWS access key
- **Secret Key:** Your AWS secret key
- **ID:** `aws-creds`

#### 4. Create Jenkins Pipeline Job

1. Jenkins Dashboard → New Item
2. **Name:** `python-app-pipeline`
3. **Type:** `Pipeline`
4. **Definition:** `Pipeline script from SCM`
5. **SCM:** `Git`
6. **Repository URL:** `https://github.com/BhathiyaVicum/python-app-pipeline.git`
7. **Branch:** `main`
8. **Script Path:** `Jenkinsfile`

#### 5. Run the Pipeline

1. Click **Build Now**
2. Once complete, the application URL will be displayed:

```bash
=========================================
APPLICATION DEPLOYED!
http://54.90.201.110:5000
=========================================
```

#### 6. Access the Application

Open your browser and visit:

```
http://<EC2-PUBLIC-IP>:5000
```

## 🧪 Testing the Application

### Verify Locally on EC2

```bash
# SSH into EC2
ssh -i your-key.pem ec2-user@<EC2-PUBLIC-IP>

# Check running containers
docker ps

# Test locally
curl http://localhost:5000

# Check container logs
docker logs my-app
```

## 🔧 Troubleshooting

| Issue | Solution |
|:---|:---|
| **Docker Permission Denied** | `sudo usermod -aG docker $USER && exit` |
| **Jenkins Can't Connect to Docker** | Run Jenkins as Administrator |
| **EC2 Not Accessible** | Check Security Group inbound rules |
| **Terraform Apply Fails** | Verify AWS credentials |
| **Container Not Starting** | SSH to EC2: `docker logs my-app` |
| **user_data.sh Not Running** | `sudo cat /var/log/cloud-init-output.log` |

### Debugging EC2

```bash
ssh -i your-key.pem ec2-user@<EC2-PUBLIC-IP>

# Check Docker status
sudo systemctl status docker

# Check running containers
docker ps -a

# Check container logs
docker logs my-app

# Check user_data execution
sudo cat /var/log/cloud-init-output.log

# Test application locally
curl http://localhost:5000
```

## 📚 What I Learned

- ✅ **CI/CD Pipeline Design** – End-to-end automation with Jenkins
- ✅ **Infrastructure as Code** – Terraform best practices
- ✅ **Containerization** – Docker packaging and deployment
- ✅ **Cloud Automation** – AWS resource provisioning
- ✅ **DevOps Best Practices** – Security, automation, and cost optimization
- ✅ **Pipeline as Code** – Declarative Jenkinsfile syntax

---

⭐ Star this repository if you found it helpful!

## 📊 Project Status

[![GitHub last commit](https://img.shields.io/github/last-commit/BhathiyaVicum/python-app-pipeline)](https://github.com/BhathiyaVicum/python-app-pipeline)
[![GitHub repo size](https://img.shields.io/github/repo-size/BhathiyaVicum/python-app-pipeline)](https://github.com/BhathiyaVicum/python-app-pipeline)
[![GitHub stars](https://img.shields.io/github/stars/BhathiyaVicum/python-app-pipeline)](https://github.com/BhathiyaVicum/python-app-pipeline)
