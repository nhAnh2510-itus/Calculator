pipeline {
    agent {
        label 'window-agent'
    }

    environment {
        BUILD_TAG = "${BUILD_NUMBER}"
        PYTHON_HOME = "C:\\Python312"
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
                    bat '''
                        python -m venv venv
                        call venv\\Scripts\\activate.bat
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
                    bat '''
                        call venv\\Scripts\\activate.bat
                        pytest tests/ -v
                    '''
                }
            }
        }

        stage('Generate Code Coverage Report') {
            steps {
                echo '===== Generating Coverage Report ====='
                dir('backend') {
                    bat '''
                        call venv\\Scripts\\activate.bat
                        pytest tests/ --cov=app --cov-report=xml --cov-report=html -v
                    '''
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                echo '===== Building Docker Images ====='
                bat '''
                    echo Building Backend Docker Image...
                    docker build -t calculator-backend:%BUILD_TAG% -t calculator-backend:latest ./backend
                    
                    echo Building Frontend Docker Image...
                    docker build -t calculator-frontend:%BUILD_TAG% -t calculator-frontend:latest ./frontend
                    
                    echo ✓ Docker images built successfully
                    docker images | find "calculator"
                '''
            }
        }

        stage('Deploy Docker Containers') {
            steps {
                echo '===== Deploying Docker Containers ====='
                bat '''
                    echo Stopping old containers...
                    docker stop calculator-backend 2>nul || echo "No container to stop"
                    docker stop calculator-frontend 2>nul || echo "No container to stop"
                    docker rm calculator-backend 2>nul || echo "No container to remove"
                    docker rm calculator-frontend 2>nul || echo "No container to remove"
                    timeout /t 2 /nobreak
                    
                    echo Starting Backend Container...
                    docker run -d ^
                        --name calculator-backend ^
                        -p 8000:8000 ^
                        calculator-backend:%BUILD_TAG%
                    
                    echo Starting Frontend Container...
                    docker run -d ^
                        --name calculator-frontend ^
                        -p 80:80 ^
                        calculator-frontend:%BUILD_TAG%
                    
                    timeout /t 3 /nobreak
                    
                    echo ✓ Containers started successfully
                    docker ps | find "calculator"
                '''
            }
        }
    }

    post {
        always {
            echo '===== Post Build Actions ====='
            
            archiveArtifacts artifacts: 'backend/coverage.xml', allowEmptyArchive: true
            archiveArtifacts artifacts: 'backend/htmlcov/**', allowEmptyArchive: true
        }

        success {
            echo '✓ Build and Deployment Successful!'
            echo '════════════════════════════════════════════'
            echo '📍 Backend: http://localhost:8000'
            echo '📍 Frontend: http://localhost:80'
            echo '📍 API Docs: http://localhost:8000/docs'
            echo '════════════════════════════════════════════'
        }

        failure {
            echo '✗ Build or Deployment Failed!'
            bat '''
                echo === Docker Images ===
                docker images | find "calculator" || echo "No images found"
                
                echo === Running Containers ===
                docker ps | find "calculator" || echo "No containers running"
            '''
        }
    }
}
