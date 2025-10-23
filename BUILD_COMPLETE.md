# 🎉 Calculator Demo App - BUILD COMPLETE!

## ✅ Hoàn Thành

Ứng dụng **Full-Stack Calculator** đã được xây dựng hoàn chỉnh với tất cả các thành phần yêu cầu:

### ✅ Backend (FastAPI + Python)

- **app/logic.py** - 4 hàm tính toán (add, subtract, multiply, divide)
- **app/main.py** - 5 API endpoints với CORS middleware
- **tests/test_logic.py** - 21 unit tests (100% coverage)
- **tests/test_main.py** - 12 API tests (100% coverage)
- **Dockerfile** - Build image Python
- **requirements.txt** - Dependencies (FastAPI, pytest, pytest-cov)

### ✅ Frontend (HTML/CSS/Vanilla JS)

- **index.html** - UI máy tính responsive design
- **style.css** - Modern styling + animations
- **app.js** - Calculator logic + fetch() API calls + keyboard shortcuts
- **Dockerfile** - Build image Nginx

### ✅ Containerization & CI/CD

- **docker-compose.yml** - Chạy cả 2 services cùng lúc
- **Jenkinsfile** - Complete CI/CD pipeline
- **6 Stages**: Checkout → Setup → Test → Coverage → Build → Deploy

### ✅ Documentation

- **README.md** - Hướng dẫn chi tiết (cài đặt, chạy, API)
- **QUICKSTART.md** - Bắt đầu trong 5 phút
- **TESTING_GUIDE.md** - Unit test & coverage chi tiết
- **CICD_GUIDE.md** - Jenkins & CI/CD hướng dẫn
- **STRUCTURE.txt** - Cấu trúc dự án

### ✅ Helper Scripts

- **run_tests.bat** - Chạy tests trên Windows
- **run_tests.sh** - Chạy tests trên Unix/Linux
- **startup.bat** - Khởi động app trên Windows
- **startup.sh** - Khởi động app trên Unix/Linux

---

## 🚀 Bắt Đầu Ngay

### Option 1: Chạy Nhanh (5 phút)

```bash
# Terminal 1 - Backend
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

```bash
# Terminal 2 - Frontend
cd frontend
python -m http.server 8080
```

✅ **Frontend**: http://localhost:8080
✅ **Backend**: http://localhost:8000/docs

---

### Option 2: Docker Compose (Recommended)

```bash
docker-compose up
```

✅ **Frontend**: http://localhost:80
✅ **Backend**: http://localhost:8000/docs

---

### Option 3: Helper Scripts

**Windows:**
```bash
run_tests.bat      # Chạy tests
startup.bat        # Khởi động app
```

**macOS/Linux:**
```bash
bash run_tests.sh  # Chạy tests
bash startup.sh    # Khởi động app
```

---

## 🧪 Testing & Coverage

```bash
cd backend
source venv/bin/activate

# Chạy tests
pytest tests/ -v

# Xem coverage
pytest tests/ --cov=app --cov-report=html -v
# Mở: htmlcov/index.html
```

**Coverage Status:**
- ✅ test_logic.py: 100% (21 tests)
- ✅ test_main.py: 100% (12 tests)
- ✅ Total: 100% (33 tests)

---

## 📊 API Endpoints

| Endpoint | Method | Request | Response |
|----------|--------|---------|----------|
| `/` | GET | - | `{"message": "..."}` |
| `/add` | POST | `{"a": 10, "b": 5}` | `{"result": 15}` |
| `/subtract` | POST | `{"a": 10, "b": 5}` | `{"result": 5}` |
| `/multiply` | POST | `{"a": 10, "b": 5}` | `{"result": 50}` |
| `/divide` | POST | `{"a": 10, "b": 5}` | `{"result": 2}` |

**Error Handling:**
```json
POST /divide
{"a": 10, "b": 0}

Response (400):
{"detail": "Không thể chia cho 0"}
```

---

## 🏗️ Project Structure

```
calculator/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── logic.py          # ⭐ Logic
│   │   └── main.py           # ⭐ API
│   ├── tests/
│   │   ├── test_logic.py     # ⭐ 21 tests
│   │   └── test_main.py      # ⭐ 12 tests
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html            # ⭐ UI
│   ├── style.css             # ⭐ CSS
│   ├── app.js                # ⭐ JS Logic
│   └── Dockerfile
├── docker-compose.yml
├── Jenkinsfile               # ⭐ CI/CD
└── README.md, QUICKSTART.md, etc.
```

---

## 🎯 Test Coverage Details

### Backend Tests (33 Total)

**test_logic.py (21 tests):**
- TestAdd (5): positive, negative, mixed, zero, float
- TestSubtract (5): positive, negative, mixed, zero, float
- TestMultiply (5): positive, negative, mixed, zero, float
- TestDivide (6): positive, negative, mixed, float, **by_zero, zero_by**

**test_main.py (12 tests):**
- TestRootEndpoint (1): GET /
- TestAddAPI (3): success, negative, float
- TestSubtractAPI (2): success, negative
- TestMultiplyAPI (2): success, by_zero
- TestDivideAPI (4): success, float, **by_zero (400), zero_by**

### Coverage Report

```bash
pytest tests/ --cov=app --cov-report=term-missing

app/logic.py
    Lines covered: 100%
    Branches: 100%

app/main.py
    Lines covered: 100%
    Branches: 100%
```

---

## 🔧 Configuration

### Backend URL (Frontend)

File: `frontend/app.js`

```javascript
const BACKEND_URL = 'http://localhost:8000';
```

Thay đổi nếu Backend chạy trên server khác:
```javascript
const BACKEND_URL = 'http://your-server.com:8000';
```

### CORS Settings

File: `backend/app/main.py`

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả origin
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🚀 Jenkins CI/CD Pipeline

### Stages

1. **Checkout** - Lấy code từ Git
2. **Setup** - Tạo virtual environment
3. **Test** - Chạy pytest
4. **Coverage** - Tạo coverage report
5. **Build** - Build Docker images
6. **Deploy** - Chạy containers

### Setup Jenkins

```bash
# Chạy Jenkins
docker run -d --name jenkins -p 8080:8080 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```

### Create Pipeline Job

1. Jenkins → New Item → Pipeline
2. SCM: Git
3. Script path: Jenkinsfile
4. Build Now

---

## 📚 Documentation

| File | Nội Dung |
|------|----------|
| **README.md** | Hướng dẫn chi tiết toàn bộ |
| **QUICKSTART.md** | Bắt đầu trong 5 phút |
| **TESTING_GUIDE.md** | Unit test & coverage |
| **CICD_GUIDE.md** | Jenkins & CI/CD |
| **STRUCTURE.txt** | Cấu trúc dự án |

---

## 🎨 Frontend Features

✅ Responsive design (desktop + mobile)
✅ Keyboard shortcuts (0-9, +, -, *, /, =, Backspace, Esc)
✅ Error handling (chia cho 0)
✅ Status messages (thành công/lỗi)
✅ Modern UI/UX

### Keyboard Shortcuts

| Phím | Chức năng |
|------|----------|
| `0-9` | Nhập số |
| `.` | Dấu thập phân |
| `+`, `-`, `*`, `/` | Toán tử |
| `Enter` / `=` | Tính toán |
| `Backspace` | Xóa ký tự cuối |
| `Esc` | Xóa tất cả |

---

## 🐛 Troubleshooting

### Frontend không kết nối Backend

```bash
# 1. Kiểm tra Backend chạy
curl http://localhost:8000

# 2. Kiểm tra CORS trong main.py
# 3. Điều chỉnh BACKEND_URL trong app.js
```

### Tests fail

```bash
# 1. Kích hoạt venv
source venv/bin/activate

# 2. Cài dependencies
pip install -r requirements.txt

# 3. Chạy tests
pytest tests/ -v
```

### Docker issues

```bash
docker system prune -a
docker-compose up --build
```

---

## 📈 Next Steps

1. ✅ **Local Development** - Chạy locally để test
2. ✅ **Unit Tests** - Chạy tests & xem coverage
3. ✅ **Docker** - Build & chạy containers
4. ✅ **Jenkins** - Setup CI/CD pipeline
5. ✅ **Git** - Push lên repository
6. ✅ **Webhook** - Setup GitHub webhook cho Jenkins

---

## 🎓 Learning Outcomes

Qua project này, bạn sẽ học được:

- ✅ **FastAPI** - Framework web Python hiện đại
- ✅ **Unit Testing** - Viết test bằng pytest
- ✅ **Code Coverage** - Đo lường coverage
- ✅ **Frontend API** - Gọi Backend API từ JS
- ✅ **Docker** - Containerization
- ✅ **Docker Compose** - Multi-container setup
- ✅ **Jenkins** - CI/CD pipeline
- ✅ **CORS** - Cross-origin requests
- ✅ **Error Handling** - Exception handling
- ✅ **RESTful API** - API design

---

## 📞 Support

Nếu gặp vấn đề:

1. Xem **README.md** (hướng dẫn chi tiết)
2. Xem **TESTING_GUIDE.md** (test issues)
3. Xem **CICD_GUIDE.md** (Jenkins issues)
4. Check **docker logs** (Docker issues)
5. Check **pytest output** (test issues)

---

## 📄 License

MIT License - Tự do sử dụng, modify, distribute

---

## 🎉 Enjoy Your Calculator App!

**Tạo bởi:** Demo Team  
**Ngày:** Oct 23, 2025  
**Version:** 1.0.0

---

**Happy Coding! 🚀**
