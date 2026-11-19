
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
                bat 'docker --version'
                
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
