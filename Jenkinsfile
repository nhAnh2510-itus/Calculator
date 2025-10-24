pipeline {
    agent {
        docker {
            image 'python:3.10-slim'  
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        BUILD_TAG = "${BUILD_NUMBER}"
        REGISTRY = "localhost"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '===== Checkout Code ====='
                checkout scm
            }
        }

        stage('Setup Backend Environment') {
            steps {
                echo '===== Setup Python Environment ====='
                dir('backend') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Backend Tests') {
            steps {
                echo '===== Running Unit Tests ====='
                dir('backend') {
                    sh '''
                        . venv/bin/activate
                        pytest tests/ -v
                    '''
                }
            }
        }

        stage('Generate Code Coverage Report') {
            steps {
                echo '===== Generating Coverage Report ====='
                dir('backend') {
                    sh '''
                        . venv/bin/activate
                        pytest tests/ --cov=app --cov-report=xml --cov-report=html -v
                    '''
                }
            }
        }

        stage('Build Docker Images') {
            agent {
                label 'window-agent'
            }
            steps {
                echo '===== Building Docker Images ====='
                sh '''
                    echo "Building Backend Docker Image..."
                    docker build -t calculator-backend:${BUILD_TAG} -t calculator-backend:latest ./backend
                    
                    echo "Building Frontend Docker Image..."
                    docker build -t calculator-frontend:${BUILD_TAG} -t calculator-frontend:latest ./frontend
                    
                    echo "✓ Docker images built successfully"
                    docker images | grep calculator
                '''
            }
        }

        stage('Deploy Docker Containers') {
            agent {
                label 'window-agent'
            }
            steps {
                echo '===== Deploying Docker Containers ====='
                sh '''
                    # Stop and remove old containers
                    echo "Stopping old containers..."
                    docker stop calculator-backend 2>/dev/null || true
                    docker stop calculator-frontend 2>/dev/null || true
                    docker rm calculator-backend 2>/dev/null || true
                    docker rm calculator-frontend 2>/dev/null || true
                    sleep 2
                    
                    # Run new containers
                    echo "Starting Backend Container..."
                    docker run -d \
                        --name calculator-backend \
                        -p 8000:8000 \
                        --log-driver json-file \
                        --log-opt max-size=10m \
                        --log-opt max-file=3 \
                        calculator-backend:${BUILD_TAG}
                    
                    echo "Starting Frontend Container..."
                    docker run -d \
                        --name calculator-frontend \
                        -p 80:80 \
                        --log-driver json-file \
                        --log-opt max-size=10m \
                        --log-opt max-file=3 \
                        calculator-frontend:${BUILD_TAG}
                    
                    sleep 3
                    
                    echo "✓ Containers started successfully"
                    docker ps | grep calculator
                '''
            }
        }
    }

    post {
        always {
            echo '===== Post Build Actions ====='

            // Publish coverage report
            publishHTML(target: [
                reportDir: 'backend/htmlcov',
                reportFiles: 'index.html',
                reportName: 'Coverage Report'
            ])

            // Archive artifacts
            archiveArtifacts artifacts: 'backend/coverage.xml', allowEmptyArchive: true
        }

        success {
            echo '✓ Build and Deployment Successful!'
            echo '════════════════════════════════════════════'
            echo '📍 Backend: http://localhost:8000'
            echo '📍 Frontend: http://localhost:80'
            echo '📍 API Docs: http://localhost:8000/docs'
            echo '📍 Coverage: Jenkins Dashboard'
            echo '════════════════════════════════════════════'
        }

        failure {
            echo '✗ Build or Deployment Failed!'
            sh '''
                echo "=== Docker Images ===" && docker images | grep calculator || true
                echo "=== Running Containers ===" && docker ps | grep calculator || true
            '''
        }
    }
}
