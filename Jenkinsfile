pipeline {
    agent any
    
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
                        python -m venv venv
                        . venv/bin/activate
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
            steps {
                echo '===== Building Docker Images ====='
                sh '''
                    docker build -t calculator-backend:${BUILD_NUMBER} ./backend
                    docker build -t calculator-frontend:${BUILD_NUMBER} ./frontend
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                echo '===== Deploying Application ====='
                sh '''
                    # Stop existing containers if any
                    docker stop calculator-backend 2>/dev/null || true
                    docker stop calculator-frontend 2>/dev/null || true
                    
                    # Run new containers
                    docker run -d --name calculator-backend -p 8000:8000 calculator-backend:${BUILD_NUMBER}
                    docker run -d --name calculator-frontend -p 80:80 calculator-frontend:${BUILD_NUMBER}
                    
                    echo "Backend: http://localhost:8000"
                    echo "Frontend: http://localhost:80"
                '''
            }
        }
    }
    
    post {
        always {
            echo '===== Cleanup ====='
            // Publish coverage report
            publishHTML(target: [
                reportDir: 'backend/htmlcov',
                reportFiles: 'index.html',
                reportName: 'Coverage Report'
            ])
            
            // Archive coverage XML for Cobertura plugin
            archiveArtifacts artifacts: 'backend/coverage.xml', allowEmptyArchive: true
        }
        
        success {
            echo '✓ Build and Deployment Successful!'
        }
        
        failure {
            echo '✗ Build or Deployment Failed!'
        }
    }
}
