# Calculator - CI/CD with Jenkins Guide

## 📋 Tổng Quan

Pipeline Jenkins tự động:

1. ✅ Checkout code từ Git
2. ✅ Setup Python environment
3. ✅ Chạy unit tests
4. ✅ Tạo code coverage report
5. ✅ Build Docker images
6. ✅ Deploy containers

## 🚀 Setup Jenkins

### 1. Cài đặt Jenkins (Docker)

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

### 2. Lấy Initial Admin Password

```bash
docker logs jenkins | grep "Please use the following password"
```

### 3. Truy cập Jenkins

Mở browser: `http://localhost:8080`

- Username: `admin`
- Password: (từ bước 2)

### 4. Cài đặt Recommended Plugins

- Jenkins sẽ yêu cầu cài plugins
- Chọn **Install suggested plugins**
- Chờ cài đặt hoàn tất

### 5. Cài đặt Plugins Bổ sung

**Manage Jenkins** → **Manage Plugins** → **Available Plugins**

Tìm và cài đặt:

- **HTML Publisher Plugin** (để hiển thị coverage report)
- **Cobertura Plugin** (để parse coverage.xml)
- **Pipeline Plugin** (nếu chưa có)
- **Git Plugin**

## 🔧 Tạo Pipeline Job

### Method 1: Declarative Pipeline (Recommended)

#### Bước 1: Tạo Job

1. **New Item**
2. Nhập tên: `calculator-pipeline`
3. Chọn **Pipeline**
4. **OK**

#### Bước 2: Cấu hình Pipeline

**Pipeline** section:

- **Definition:** `Pipeline script from SCM`
- **SCM:** `Git`
- **Repository URL:** `https://github.com/your-username/calculator.git`
- **Branches to build:** `*/main` (hoặc branch của bạn)
- **Script path:** `Jenkinsfile`

#### Bước 3: Save & Build

Nhấn **Save** → **Build Now**

### Method 2: Inline Jenkinsfile (Testing)

Nếu chưa có Git, dùng inline:

**Pipeline** section:

- **Definition:** `Pipeline script`
- Copy-paste nội dung `Jenkinsfile` vào text area

```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo '===== Checkout Code ====='
                checkout scm
            }
        }
        // ... stages khác
    }
}
```

## 📊 Pipeline Stages

### Stage 1: Checkout

```groovy
stage('Checkout') {
    steps {
        echo '===== Checkout Code ====='
        checkout scm
    }
}
```

✅ **Lấy code từ Git repository**

### Stage 2: Setup Backend Environment

```groovy
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
```

✅ **Tạo virtual environment và cài đặt dependencies**

### Stage 3: Run Backend Tests

```groovy
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
```

✅ **Chạy unit tests - build fail nếu test fail**

### Stage 4: Generate Code Coverage Report

```groovy
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
```

✅ **Tạo coverage reports (XML + HTML)**

### Stage 5: Build Docker Images

```groovy
stage('Build Docker Images') {
    steps {
        echo '===== Building Docker Images ====='
        sh '''
            docker build -t calculator-backend:${BUILD_NUMBER} ./backend
            docker build -t calculator-frontend:${BUILD_NUMBER} ./frontend
        '''
    }
}
```

✅ **Build Docker images với tag build number**

### Stage 6: Deploy

```groovy
stage('Deploy') {
    steps {
        echo '===== Deploying Application ====='
        sh '''
            # Stop existing containers
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
```

✅ **Deploy containers**

## 📈 Post Actions

```groovy
post {
    always {
        echo '===== Cleanup ====='
        
        // Publish HTML coverage report
        publishHTML(target: [
            reportDir: 'backend/htmlcov',
            reportFiles: 'index.html',
            reportName: 'Coverage Report'
        ])
        
        // Archive coverage XML
        archiveArtifacts artifacts: 'backend/coverage.xml', allowEmptyArchive: true
    }
    
    success {
        echo '✓ Build and Deployment Successful!'
    }
    
    failure {
        echo '✗ Build or Deployment Failed!'
    }
}
```

✅ **Publish reports, archive artifacts**

## 🎯 Xem Build Results

### 1. Console Output

Trong job: **Build #X** → **Console Output**

Xem tất cả logs từ từng stage

### 2. Coverage Report

Trong job: **Coverage Report**

Xem chi tiết coverage cho mỗi file

### 3. Artifacts

Trong job: **Build Artifacts**

Download coverage.xml, log files, etc.

## 🔄 Trigger Builds

### Manual Trigger

- Nhấn **Build Now** trong job

### Poll SCM

**Build Triggers** → **Poll SCM**

```
H/15 * * * *
```

(Kiểm tra Git mỗi 15 phút)

### Webhook (GitHub)

**Build Triggers** → **GitHub hook trigger**

Cấu hình GitHub repo settings:

- **Webhooks** → **Add webhook**
- **Payload URL:** `http://your-jenkins:8080/github-webhook/`
- **Content type:** `application/json`

## 🐛 Troubleshooting

### Error: "docker: command not found"

Jenkins agent cần cài Docker:

```bash
docker exec jenkins docker ps  # Check if Docker socket mounted
```

Nếu lỗi, mount Docker socket:

```bash
docker stop jenkins
docker rm jenkins
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

### Error: "Permission denied while trying to connect"

```bash
# Trong Jenkins container
docker exec jenkins usermod -aG docker jenkins
```

Restart Jenkins:

```bash
docker restart jenkins
```

### Error: "Python: No module named venv"

```bash
# Trong Jenkins agent
docker exec jenkins apt-get update && apt-get install -y python3-venv
```

### Build Unstable (Tests Pass But Coverage Low)

Thêm coverage threshold:

```groovy
stage('Check Coverage') {
    steps {
        dir('backend') {
            sh 'pytest tests/ --cov=app --cov-fail-under=80'
        }
    }
}
```

## 📋 Webhook GitHub Integration

### Bước 1: Tạo Personal Access Token

1. GitHub → **Settings** → **Developer settings** → **Personal access tokens**
2. **Generate new token**
3. Scopes: `repo`, `admin:repo_hook`
4. Copy token

### Bước 2: Cấu hình Jenkins

**Manage Jenkins** → **Configure System**

**GitHub** section:

- **GitHub Server:** Add
- **API URL:** `https://api.github.com`
- **Credentials:** Add → Enter token
- **Test connection**

### Bước 3: Cấu hình Repository

GitHub repo → **Settings** → **Webhooks**

- **Payload URL:** `http://your-jenkins:8080/github-webhook/`
- **Content type:** `application/json`
- **Events:** Push events
- **Active:** ✓

## 📊 Metrics & Reporting

### Jenkins Dashboard

Cài **Metrics Plugin** để xem:

- Build success rate
- Average build time
- Coverage trends

### Pipeline Notifications

Thêm vào Jenkinsfile:

```groovy
post {
    failure {
        // Email notification
        emailext(
            subject: "Build Failed: ${JOB_NAME} #${BUILD_NUMBER}",
            body: "Check build logs: ${BUILD_URL}",
            to: 'team@example.com'
        )
    }
}
```

## 🚀 Advanced Pipeline

### Parallel Stages

```groovy
parallel(
    'Build Backend': {
        dir('backend') {
            sh 'docker build -t calculator-backend:latest .'
        }
    },
    'Build Frontend': {
        dir('frontend') {
            sh 'docker build -t calculator-frontend:latest .'
        }
    }
)
```

### Conditional Stages

```groovy
stage('Deploy to Production') {
    when {
        branch 'main'
    }
    steps {
        echo 'Deploying to production...'
    }
}
```

### Input Steps

```groovy
stage('Approve Deploy') {
    steps {
        input(
            id: 'Proceed',
            message: 'Ready to deploy?',
            ok: 'Deploy'
        )
    }
}
```

## 📚 Tài liệu Tham Khảo

- [Jenkins Documentation](https://www.jenkins.io/doc)
- [Pipeline Syntax Reference](https://www.jenkins.io/doc/book/pipeline/syntax)
- [GitHub Integration](https://plugins.jenkins.io/github)

---

**Happy CI/CD! 🚀**
