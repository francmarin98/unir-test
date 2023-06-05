/* groovylint-disable CompileStatic, DuplicateStringLiteral, LineLength */
pipeline {
    agent any

    stages {
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
            sh """curl -X POST https://api.sendgrid.com/v3/mail/send \
                -H 'Content-Type: application/json' \
                -H 'Authorization: Bearer ${SENDGRID_API_KEY}' \
                -d '{
                    \"personalizations\": [
                        {
                            \"to\": [
                                {
                                    \"email\": \"${TO_EMAIL}\"
                                }
                            ]
                        }
                    ],
                    \"from\": {
                        \"email\": \"${FROM_EMAIL}\"
                    },
                    \"subject\": \"Subject - Build ${env.BUILD_NUMBER} ${currentBuild.currentResult}\",
                    \"content\": [
                        {
                            \"type\": \"text/plain\",
                            \"value\": \"La ejecución del pipeline fue exitosa\"
                        }
                    ]
                }'"""
            echo 'Email Notification!'
            echo "${currentBuild.currentResult}: Job ${env.JOB_NAME}\nBuild Number: ${env.BUILD_NUMBER}\nMore Info can be found here: ${env.BUILD_URL}"
            cleanWs()
        }
        failure {
            sh """curl -X POST https://api.sendgrid.com/v3/mail/send \
                -H 'Content-Type: application/json' \
                -H 'Authorization: Bearer ${SENDGRID_API_KEY}' \
                -d '{
                    \"personalizations\": [
                        {
                            \"to\": [
                                {
                                    \"email\": \"${TO_EMAIL}\"
                                }
                            ]
                        }
                    ],
                    \"from\": {
                        \"email\": \"${FROM_EMAIL}\"
                    },
                    \"subject\": \"Build ${env.BUILD_NUMBER} Failed - ${env.JOB_NAME}\",
                    \"content\": [
                        {
                            \"type\": \"text/plain\",
                            \"value\": \"La ejecución del pipeline fue fracasó\"
                        }
                    ]
                }'"""
            echo 'Email Notification!'
            echo "${currentBuild.currentResult}: Job ${env.JOB_NAME}\nBuild Number: ${env.BUILD_NUMBER}\nMore Info can be found here: ${env.BUILD_URL}"
        }
    }
}
