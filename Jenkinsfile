
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Starting Flask Docker CI/CD Project'
            }
        }
        stage('Build Docker image'){
            steps{
                bat '"C:/Users/Dharmesh Nayak/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe" build -t cicd-demo1:latest .'
            }
        }
         stage('Run Docker conatiner'){
            steps{
                bat '"C:/Users/Dharmesh Nayak/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe" run -d -p 6000:5000 --name cicd-conta cicd-demo1:latest '
            }
        }
         stage('checking conatiner'){
            steps{
                bat '"C:/Users/Dharmesh Nayak/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe" ps '
            }
        }

        stage('Build') {
            steps {
                echo 'Preparing Docker Build'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Flask Application'
            }
        }

        stage('Complete') {
            steps {
                echo 'Jenkins Pipeline Executed Successfully!'
            }
        }
    }
}
