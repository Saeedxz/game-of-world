pipeline {
    agent any

    stages {
        stage('Checkout code') {
            steps {
                checkout scmGit(branches: [[name: '*/master']],
                extensions: [], userRemoteConfigs: [[credentialsId: 'github-jenkis', url: 'https://github.com/Saeedxz/game-of-world.git']])
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Run Build') {
            steps {
                sh 'docker-compose up -d'
                echo "Docker Up"
            }
        }
        stage('Test') {
            steps {
                    script {
                        try{
                            sh 'pip install -r requirements.txt'
                            sh 'python3 tests/e2e.py'
                            echo "Test PASSED"
                        }
                        catch (e) {
                            echo "Test FAILED"
                            currentBuild.result = "FAILURE"
                            currentStage.result = "FAILURE"
                        } 
                    }
            }
        }
        stage('Push Image To Docker Hub'){
            steps{
                echo "docker push <hub-user>/<repo-name>:<tag>"
            }
        }
        stage('Terminate Container'){
            steps{
                sh 'docker-compose down'
                echo "Docker Down"
            }
        }
        stage('Delete Image'){
            steps{
                sh 'docker rmi saeed/wog:latest'
                echo "Image removed"
            }
        }
    }
}