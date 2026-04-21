pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/stanishq2710/2022BCS0183-mlops-assignment.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip3 install -r requirements.txt
                pip3 install "dvc[s3]"
                '''
            }
        }

        stage('DVC Pull') {
            steps {
                sh '''
                dvc pull
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                python3 src/train.py
                '''
            }
        }

        stage('List Files (Debug)') {
            steps {
                sh '''
                ls
                '''
            }
        }
    }
}
