pipeline {
    agent {
        docker {
            image 'python:3.5.1'
        }
    }

    stages {
        stage('AddSub') {
            steps {
                sh 'python -m unittest tests.TestAddSub'
            }
        }
        stage('MulDiv') {
            steps {
                sh 'python -m unittest tests.TestMulDiv'
            }
        }
    }
}
