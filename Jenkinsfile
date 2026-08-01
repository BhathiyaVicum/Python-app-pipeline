pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'bhathiyavi'
        IMAGE_TAG = 'v1'
    }

    stages {

        stage('Git clone') {
            steps {
                git branch: 'main', changelog: false, poll: false, url: 'https://github.com/BhathiyaVicum/python-app-pipeline/'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKERHUB_USER}/python-app-2:${IMAGE_TAG} .'
            }
        }

        stage('Push Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
    
                    sh '''
                    echo $DOCKER_PASSWORD | docker login \
                    -u $DOCKER_USERNAME \
                    --password-stdin
                    
                    docker push ${DOCKERHUB_USER}/python-app-2:${IMAGE_TAG}
                    '''
    
                    }
            }
        }

        stage('Terraform Deploy') {
            steps {
               
               withCredentials([
                aws(
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    credentialsId: 'aws-creds',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                    )
                ]) {
                    dir('terraform') {
                        sh '''
                            terraform init
                            terraform apply -auto-approve \
                                -var="docker_hub_username=${DOCKERHUB_USER}" \
                                -var="image_tag=${IMAGE_TAG}"
                        '''
                    }
                }

            }
        }

        stage('Get URL') {
            steps {
                script {
                    dir('terraform') {
                        def public_ip = sh(
                            script: 'terraform output -raw public_ip',
                            returnStdout: true
                        ).trim()
                        echo "========================================="
                        echo "APPLICATION DEPLOYED!"
                        echo "http://${public_ip}:5000"
                        echo "========================================="
                    }
                }
            }
        }

    }
}
