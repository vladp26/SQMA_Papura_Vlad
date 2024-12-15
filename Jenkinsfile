pipeline {
    agent any

    stages {
        stage('AddSub') {
            steps {
                bat 'python -m unittest tests.TestAddSub'
            }
        }
        stage('MulDiv') {
            steps {
                bat 'python -m unittest tests.TestMulDiv'
            }
        }
    }
}
