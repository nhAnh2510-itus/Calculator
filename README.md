# Calculator Demo App - Hướng dẫn Cài đặt & Chạy

Đây là ứng dụng **Full-Stack Calculator** được xây dựng để demo:
- ✅ **Unit Testing** (pytest)
- ✅ **Code Coverage** (pytest-cov)
- ✅ **CI/CD** (Jenkins)
- ✅ **Containerization** (Docker)

## 📋 Yêu cầu

- Python 3.10+
- Docker & Docker Compose
- Node.js (tùy chọn, nếu cần)
- Jenkins (cho CI/CD)

## 🏗️ Cấu trúc Dự án

```
calculator/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── logic.py          # Logic tính toán (add, subtract, multiply, divide)
│   │   └── main.py           # FastAPI endpoints
│   ├── tests/
│   │   ├── test_logic.py     # Unit tests cho logic
│   │   └── test_main.py      # API tests
│   ├── requirements.txt       # Python dependencies
│   └── Dockerfile            # Docker image cho Backend
│
├── frontend/
│   ├── index.html            # UI máy tính
│   ├── style.css             # Styling
│   ├── app.js                # JavaScript logic
│   └── Dockerfile            # Docker image cho Frontend
│
└── Jenkinsfile               # CI/CD pipeline
```

## 🚀 Chạy Ứng dụng Locally (Không Docker)

### 1. Chạy Backend

```bash
cd backend

# Tạo virtual environment
python -m venv venv

# Kích hoạt virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy server
uvicorn app.main:app --reload
```

Backend sẽ chạy tại: `http://localhost:8000`

**API Documentation:** `http://localhost:8000/docs`

### 2. Chạy Frontend

Mở file `frontend/index.html` trực tiếp trong browser, hoặc dùng HTTP server:

```bash
cd frontend

# Python 3.10+
python -m http.server 8080

# Hoặc dùng Node.js http-server
npx http-server
```

Frontend sẽ chạy tại: `http://localhost:8080`

## 🧪 Chạy Unit Tests & Code Coverage

```bash
cd backend

# Kích hoạt virtual environment
source venv/bin/activate  # hoặc venv\Scripts\activate trên Windows

# Chạy tất cả tests
pytest tests/ -v

# Chạy tests và generate coverage report
pytest tests/ --cov=app --cov-report=html --cov-report=xml -v

# Xem HTML coverage report
# Mở: htmlcov/index.html trong browser
```

## 🐳 Chạy với Docker

### 1. Build Images

```bash
# Build Backend image
docker build -t calculator-backend:latest ./backend

# Build Frontend image
docker build -t calculator-frontend:latest ./frontend
```

### 2. Chạy Containers

```bash
# Chạy Backend
docker run -d --name calculator-backend -p 8000:8000 calculator-backend:latest

# Chạy Frontend
docker run -d --name calculator-frontend -p 80:80 calculator-frontend:latest
```

### 3. Truy cập Ứng dụng

- Backend API: `http://localhost:8000`
- Frontend: `http://localhost:80`

### 4. Dừng Containers

```bash
docker stop calculator-backend calculator-frontend
docker rm calculator-backend calculator-frontend
```

## 🐳 Chạy với Docker Compose (Nên dùng)

Tạo file `docker-compose.yml` trong thư mục gốc:

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
    networks:
      - calculator-network

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
    networks:
      - calculator-network

networks:
  calculator-network:
    driver: bridge
```

Chạy:

```bash
docker-compose up -d

# Xem logs
docker-compose logs -f

# Dừng
docker-compose down
```

## 🔧 Cấu hình Backend URL (Frontend)

Nếu Backend chạy trên máy chủ khác, chỉnh sửa `frontend/app.js`:

```javascript
const BACKEND_URL = 'http://your-backend-server:8000';
```

## 📊 CI/CD với Jenkins

### Setup Jenkins (Docker)

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
```

### Tạo Pipeline Job

1. Đăng nhập Jenkins: `http://localhost:8080`
2. Tạo **New Item** → **Pipeline**
3. Chọn **Pipeline script from SCM**
4. Chọn **Git** và nhập repository URL
5. Chỉ định **Script path**: `Jenkinsfile`
6. **Build Now**

### Pipeline Stages

- ✅ **Checkout**: Lấy code từ Git
- ✅ **Setup**: Cài đặt Python dependencies
- ✅ **Test**: Chạy unit tests
- ✅ **Coverage**: Tạo coverage report
- ✅ **Build**: Build Docker images
- ✅ **Deploy**: Chạy Docker containers

### Xem Coverage Report

1. Vào Jenkins Job → **Coverage Report**
2. Hoặc tìm HTML coverage report trong artifacts

## 📝 API Endpoints

### 1. Root

```http
GET /
```

### 2. Add (Cộng)

```http
POST /add
Content-Type: application/json

{
  "a": 10,
  "b": 5
}

Response: {"result": 15}
```

### 3. Subtract (Trừ)

```http
POST /subtract
Content-Type: application/json

{
  "a": 10,
  "b": 5
}

Response: {"result": 5}
```

### 4. Multiply (Nhân)

```http
POST /multiply
Content-Type: application/json

{
  "a": 10,
  "b": 5
}

Response: {"result": 50}
```

### 5. Divide (Chia)

```http
POST /divide
Content-Type: application/json

{
  "a": 10,
  "b": 5
}

Response: {"result": 2}
```

**Error (chia cho 0):**

```http
Status: 400 Bad Request

{
  "detail": "Không thể chia cho 0"
}
```

## 🎨 Frontend Features

- ✅ Giao diện máy tính truyền thống
- ✅ Hỗ trợ phím tắt keyboard
- ✅ Hiển thị thông báo lỗi/thành công
- ✅ Responsive design (mobile-friendly)
- ✅ Gọi Backend API qua fetch()

### Phím Tắt

| Phím | Chức năng |
|------|----------|
| `0-9` | Nhập số |
| `.` | Dấu thập phân |
| `+`, `-`, `*`, `/` | Toán tử |
| `Enter` hoặc `=` | Tính toán |
| `Backspace` | Xóa ký tự cuối |
| `Esc` | Xóa tất cả |

## 📦 Dependencies

### Backend

- `fastapi==0.104.1` - Web framework
- `uvicorn==0.24.0` - ASGI server
- `pytest==7.4.3` - Testing framework
- `pytest-cov==4.1.0` - Coverage plugin

### Frontend

- HTML5, CSS3, Vanilla JavaScript
- Không cần dependencies!

## 🐛 Troubleshooting

### Frontend không kết nối được Backend

- Kiểm tra Backend có chạy: `curl http://localhost:8000`
- Kiểm tra CORS configuration trong `backend/app/main.py`
- Chỉnh sửa `BACKEND_URL` trong `frontend/app.js`

### Tests không chạy

```bash
# Kiểm tra virtual environment
source venv/bin/activate

# Kiểm tra pytest
pytest --version

# Kiểm tra dependencies
pip list
```

### Docker build failed

```bash
# Xóa images cũ
docker system prune -a

# Build lại
docker build -t calculator-backend:latest ./backend
```

## 📚 Tài liệu Thêm

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Pytest Documentation](https://docs.pytest.org)
- [Docker Documentation](https://docs.docker.com)
- [Jenkins Documentation](https://www.jenkins.io/doc)

## 📄 License

MIT License

---

**Tạo bởi:** Demo Team  
**Ngày:** 2025
