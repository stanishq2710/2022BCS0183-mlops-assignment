pipeline {
    agent any
    
    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/stanishq2710/2022BCS0183-mlops-assignment.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                pip install "dvc[s3]"
                '''
            }
        }

        stage('DVC Pull') {
            steps {
                sh '''
                . venv/bin/activate
                dvc pull
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . venv/bin/activate
                python src/train.py
                '''
            }
        }

        stage('Debug Files') {
            steps {
                sh '''
                ls -la
                '''
            }
        }
    }
}
