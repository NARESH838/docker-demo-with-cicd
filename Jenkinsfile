
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
