pipeline {
    agent any

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
