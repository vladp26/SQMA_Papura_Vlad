pipeline {
    agent any

    stages {
        stage('AddSub') {
            steps {
                sh 'python -m unittest tests.testAddSub'
            }
        }
        stage('DivMul') {
            steps {
                sh 'python -m unittest tests.testDivMul'
            }
        }
    }
}