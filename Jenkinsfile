pipeline {
    agent {
        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    
    stages {
        stage('Check and Install Make') {
            steps {
                sh 'make --version >/dev/null 2>&1 || (apt-get update && apt-get install -y make)'
            }
        }
        
        stage('Source') {
            steps {
                git 'https://github.com/francmarin98/unir-test.git'
            }
        }

        stage('Unit tests') {
            steps {
                echo 'Unit tests!'
                sh 'make build test-unit'
                archiveArtifacts artifacts: 'results/*.xml'
                archiveArtifacts artifacts: 'results/*.html'
            }
        }

        stage('Api tests') {
            steps {
                echo 'Api tests!'
                sh 'make build test-api'
                archiveArtifacts artifacts: 'results/*.xml'
                archiveArtifacts artifacts: 'results/*.html'
            }
        }

        stage('E2e tests') {
            steps {
                echo 'E2e tests!'
                sh 'make build test-e2e'
                archiveArtifacts artifacts: 'results/*.xml'
                archiveArtifacts artifacts: 'results/*.html'
            }
        }
    }
    
    post {
        always {
            junit 'results/*_result.xml'
            emailext body: 'Test Message',
                    subject: 'Test Subject',
                    to: 'francmarin98@gmail.com'
            echo "Email Notification!"
            echo "${currentBuild.currentResult}: Job ${env.JOB_NAME}\nBuild Number: ${env.BUILD_NUMBER}\nMore Info can be found here: ${env.BUILD_URL}"
            cleanWs()
        }
        failure {
            emailext body: 'Test Message',
                    subject: 'Test Subject',
                    to: 'francmarin98@gmail.com'
            echo "Email Notification!"
            echo "${currentBuild.currentResult}: Job ${env.JOB_NAME}\nBuild Number: ${env.BUILD_NUMBER}\nMore Info can be found here: ${env.BUILD_URL}"
        }
    }
}
