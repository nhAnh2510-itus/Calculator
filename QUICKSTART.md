# 🚀 Quick Start Guide

## Chạy Nhanh (5 phút)

### Option 1: Chạy Locally (Không Docker)

#### Terminal 1 - Backend

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

✅ Backend chạy tại: `http://localhost:8000`

Docs tại: `http://localhost:8000/docs`

#### Terminal 2 - Frontend

```bash
cd frontend
python -m http.server 8080
```

✅ Frontend chạy tại: `http://localhost:8080`

---

### Option 2: Chạy với Docker Compose (Recommended)

```bash
# Từ thư mục gốc
docker-compose up -d
```

✅ Backend: `http://localhost:8000`
✅ Frontend: `http://localhost:80`

Xem logs:
```bash
docker-compose logs -f
```

Dừng:
```bash
docker-compose down
```

---

## 🧪 Chạy Unit Tests

```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate
pytest tests/ -v
```

## 📊 Xem Code Coverage

```bash
pytest tests/ --cov=app --cov-report=html -v
# Mở: htmlcov/index.html
```

## 📚 Hướng Dẫn Chi Tiết

- **Backend:** Xem `README.md`
- **Testing:** Xem `TESTING_GUIDE.md`
- **CI/CD:** Xem `CICD_GUIDE.md`

---

**Bắt đầu ngay! 🎉**
