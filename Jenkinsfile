pipeline {
    agent {
        docker {
            image 'python:3.10-slim'  
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
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

        stage('Start Backend Service') {
            steps {
                echo '===== Starting Backend Service ====='
                dir('backend') {
                    sh '''
                        . venv/bin/activate
                        pkill -f "uvicorn app.main" || true
                        sleep 2
                        nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > backend.log 2>&1 &
                        sleep 3
                        echo "✓ Backend running on http://localhost:8000"
                    '''
                }
            }
        }

        stage('Start Frontend Service') {
            steps {
                echo '===== Starting Frontend Service ====='
                sh '''
                    cd frontend
                    pkill -f "python -m http.server 8080" || true
                    sleep 2
                    nohup python -m http.server 8080 > frontend.log 2>&1 &
                    sleep 2
                    echo "✓ Frontend running on http://localhost:8080"
                '''
            }
        }
    }

    post {
        always {
            echo '===== Post Build Actions ====='

            // Publish coverage report (cần cài plugin HTML Publisher)
            publishHTML(target: [
                reportDir: 'backend/htmlcov',
                reportFiles: 'index.html',
                reportName: 'Coverage Report'
            ])

            archiveArtifacts artifacts: 'backend/coverage.xml', allowEmptyArchive: true
            archiveArtifacts artifacts: 'backend/backend.log', allowEmptyArchive: true
            archiveArtifacts artifacts: 'frontend/frontend.log', allowEmptyArchive: true
        }

        success {
            echo '✓ Build and Deployment Successful!'
            echo '📍 Backend: http://localhost:8000'
            echo '📍 Frontend: http://localhost:8080'
            echo '📍 API Docs: http://localhost:8000/docs'
        }

        failure {
            echo '✗ Build or Deployment Failed!'
            sh '''
                echo "=== Backend Log ===" && tail -20 backend/backend.log || true
                echo "=== Frontend Log ===" && tail -20 frontend/frontend.log || true
            '''
        }
    }
}
