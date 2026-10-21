pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/amansingh-develops/Jenkins-TestDemo.git'
    }

    stages {
        stage('Fetch Source Code from GitHub') {
            steps {
                echo "Fetching source code from repository: ${env.REPO_URL}"
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main'], [name: '*/master']],
                    userRemoteConfigs: [[url: env.REPO_URL]]
                ])
            }
        }

        stage('Environment & Workspace Verification') {
            steps {
                echo 'Checking workspace files and Python environment...'
                script {
                    if (isUnix()) {
                        sh 'python3 --version || python --version'
                        sh 'ls -la'
                    } else {
                        bat 'python --version'
                        bat 'dir'
                    }
                }
            }
        }

        stage('Automated Tests - Form Validation') {
            steps {
                echo 'Executing automated test suite to verify HTML Form and Input Fields...'
                script {
                    if (isUnix()) {
                        sh 'python3 test_form.py'
                    } else {
                        bat 'python test_form.py'
                    }
                }
            }
        }

        stage('Archive Build Artifacts') {
            steps {
                echo 'Archiving HTML, styles, and test scripts...'
                archiveArtifacts artifacts: '*.html, *.css, *.js, *.py', fingerprint: true, allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution cycle finished.'
        }
        success {
            echo '=================================================='
            echo 'SUCCESS: All automated tests passed successfully!'
            echo 'HTML form contains Name, Email, Contact Number, and Submit fields.'
            echo '=================================================='
        }
        failure {
            echo '=================================================='
            echo 'FAILURE: One or more automated tests failed.'
            echo 'Please review the test output logs above.'
            echo '=================================================='
        }
    }
}
