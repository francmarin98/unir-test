pipeline {
    agent any
    
    stages {
        stage('Install Docker Plugin') {
            steps {
                script {
                    // Instalar el plugin de Docker
                    def dockerPlugin = Jenkins.instance.getPlugin('docker-plugin')
                    if (!dockerPlugin) {
                        Jenkins.instance.updateCenter.install('docker-plugin')
                        Jenkins.instance.restart()
                    }
                }
            }
        }
        
        stage('Source') {
            steps {
                git 'https://github.com/francmarin98/unir-test.git'
            }
        }
        
        stage('Install Docker') {
            steps {
                sh 'curl -fsSL https://get.docker.com -o get-docker.sh'
                sh 'sh get-docker.sh'
                sh 'sudo usermod -aG docker jenkins'
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
