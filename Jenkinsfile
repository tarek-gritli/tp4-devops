pipeline {
    agent any
    environment {
        SONAR_TOKEN = credentials('sonar-token')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'uv sync'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'uv run pytest test_app.py --cov=app --cov=main --cov-report=xml --junitxml=test-results/results.xml -v'
            }
            post {
                always {
                    junit 'test-results/results.xml'
                }
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarCloud') {
                    sh '''
                        sonar-scanner \
                          -Dsonar.login=${SONAR_TOKEN}
                    '''
                }
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    dockerImage = docker.build("lgritli/tp4:${BUILD_NUMBER}")
                }
            }
}
stage('Trivy Scan') {
    steps {
        sh "trivy image --exit-code 1 --severity CRITICAL lgritli/tp4:${BUILD_NUMBER}"
    }
}
stage('Docker Push') {
    steps {
        script {
            docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-creds') {
                dockerImage.push("${BUILD_NUMBER}")
                dockerImage.push("latest")
            }
        }
    }
}
    }
}