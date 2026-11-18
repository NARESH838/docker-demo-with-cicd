
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Starting Flask Docker CI/CD Project'
            }
        }
        stage('Docker check'){
            steps{
                bat '"C:/Users/Dharmesh Nayak/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe" --version'
                bat '"C:/Users/Dharmesh Nayak/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe" info'
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
