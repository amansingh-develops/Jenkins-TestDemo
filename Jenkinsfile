pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Compile & Test') {
            steps {
                echo 'Building and testing application with Maven...'
                bat 'mvn clean test'
            }
        }

        stage('Package') {
            steps {
                echo 'Packaging application artifact...'
                bat 'mvn package -DskipTests'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'target/*.jar, index.html', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            echo '=================================================='
            echo 'SUCCESS: Maven build and packaging succeeded!'
            echo '=================================================='
        }
        failure {
            echo 'Maven build failed.'
        }
    }
}
