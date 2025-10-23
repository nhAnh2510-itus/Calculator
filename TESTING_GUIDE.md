# Calculator Backend - Unit Test Guide

## 📋 Tổng Quan

Ứng dụng backend có 2 file test:

1. **test_logic.py** - Unit tests cho `app/logic.py`
2. **test_main.py** - API tests cho `app/main.py`

**Tất cả test được viết với 100% coverage target.**

## 🧪 Chạy Tests

### 1. Setup Virtual Environment

```bash
cd backend

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Cài đặt Dependencies

```bash
pip install -r requirements.txt
```

### 3. Chạy Tất cả Tests

```bash
pytest tests/ -v
```

**Output ví dụ:**

```
tests/test_logic.py::TestAdd::test_add_positive_numbers PASSED
tests/test_logic.py::TestAdd::test_add_negative_numbers PASSED
tests/test_logic.py::TestAdd::test_add_mixed_numbers PASSED
...
tests/test_main.py::TestRootEndpoint::test_root_endpoint PASSED
tests/test_main.py::TestAddAPI::test_add_api_success PASSED
...

======================== 30 passed in 1.23s ========================
```

### 4. Chạy Tests Cụ Thể

```bash
# Chạy chỉ test_logic.py
pytest tests/test_logic.py -v

# Chạy chỉ test_main.py
pytest tests/test_main.py -v

# Chạy một test class cụ thể
pytest tests/test_logic.py::TestAdd -v

# Chạy một test function cụ thể
pytest tests/test_logic.py::TestAdd::test_add_positive_numbers -v
```

## 📊 Code Coverage

### Tạo Coverage Report

```bash
# HTML Report
pytest tests/ --cov=app --cov-report=html -v

# XML Report (cho Jenkins)
pytest tests/ --cov=app --cov-report=xml -v

# Terminal Report
pytest tests/ --cov=app -v
```

### Xem HTML Report

```bash
# File sẽ được tạo tại: htmlcov/index.html
# Mở trong browser
htmlcov/index.html
```

## 🔍 Test Coverage Details

### test_logic.py - 100% Coverage

| Hàm | Test Cases | Coverage |
|-----|-----------|----------|
| `add()` | 5 | ✅ 100% |
| `subtract()` | 5 | ✅ 100% |
| `multiply()` | 5 | ✅ 100% |
| `divide()` | 6 | ✅ 100% |

**Total: 21 test cases**

#### Các trường hợp test:

**TestAdd:**
- Cộng hai số dương
- Cộng hai số âm
- Cộng số âm và số dương
- Cộng với 0
- Cộng số thực (float)

**TestSubtract:**
- Trừ hai số dương
- Trừ hai số âm
- Trừ số âm và số dương
- Trừ với 0
- Trừ số thực

**TestMultiply:**
- Nhân hai số dương
- Nhân hai số âm
- Nhân số âm và số dương
- Nhân với 0
- Nhân số thực

**TestDivide:**
- Chia hai số dương
- Chia hai số âm
- Chia số âm và số dương
- Chia số thực
- **Chia cho 0 (Exception handling)**
- Chia 0 cho số khác

### test_main.py - 100% Coverage

| Endpoint | Test Cases | Coverage |
|----------|-----------|----------|
| GET `/` | 1 | ✅ 100% |
| POST `/add` | 3 | ✅ 100% |
| POST `/subtract` | 2 | ✅ 100% |
| POST `/multiply` | 2 | ✅ 100% |
| POST `/divide` | 4 | ✅ 100% |

**Total: 12 test cases**

#### Các trường hợp test:

**TestRootEndpoint:**
- GET / trả về message

**TestAddAPI:**
- Thêm hai số dương
- Thêm số âm
- Thêm số thực

**TestSubtractAPI:**
- Trừ hai số dương
- Trừ với số âm

**TestMultiplyAPI:**
- Nhân hai số dương
- Nhân với 0

**TestDivideAPI:**
- Chia hai số dương
- Chia số thực
- **Chia cho 0 → HTTP 400 error**
- Chia 0 cho số khác

## 🎯 Các Nguyên Tắc Test

### 1. Arrange-Act-Assert (AAA)

```python
def test_add_positive_numbers(self):
    # Arrange
    a, b = 5, 3
    
    # Act
    result = add(a, b)
    
    # Assert
    assert result == 8
```

### 2. One Assert Per Test (Nếu Có Thể)

```python
# ✅ Tốt
def test_add_positive_numbers(self):
    assert add(5, 3) == 8

def test_add_negative_numbers(self):
    assert add(-5, -3) == -8

# ❌ Không tốt
def test_add(self):
    assert add(5, 3) == 8
    assert add(-5, -3) == -8
```

### 3. Exception Testing

```python
def test_divide_by_zero(self):
    with pytest.raises(ValueError, match="Không thể chia cho 0"):
        divide(10, 0)
```

### 4. API Testing with TestClient

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_divide_api_by_zero(self):
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400
    assert "Không thể chia cho 0" in response.json()["detail"]
```

## 🛠️ Debugging Tests

### Chạy với Verbose Output

```bash
pytest tests/ -v -s
```

**Flags:**
- `-v`: Verbose (hiển thị tên từng test)
- `-s`: Show print statements
- `-x`: Stop on first failure
- `--tb=short`: Shorter traceback

### Chạy Một Test Cụ Thể

```bash
pytest tests/test_logic.py::TestDivide::test_divide_by_zero -v -s
```

### Profiling Tests

```bash
pytest tests/ --durations=10
```

## 📈 Coverage Goals

- **Target:** 100% code coverage
- **Current:** ✅ 100% achieved
- **Baseline:** 80%
- **Threshold:** 90%

### Coverage Tăng Từng Bước

```bash
# Xem coverage từng file
pytest tests/ --cov=app --cov-report=term-missing -v
```

## 🔄 Continuous Integration

### Local Pre-commit Hook

```bash
# Tạo file .git/hooks/pre-commit
#!/bin/bash
cd backend
python -m pytest tests/ --cov=app --cov-fail-under=80
```

### Jenkins Pipeline

```groovy
stage('Run Tests') {
    steps {
        dir('backend') {
            sh '''
                pytest tests/ -v --cov=app --cov-report=xml
            '''
        }
    }
}
```

## 📚 Best Practices

### ✅ Do's

- ✅ Đặt tên test function mô tả (test_divide_by_zero)
- ✅ Sử dụng fixtures cho setup/teardown
- ✅ Test cả happy path và edge cases
- ✅ Giữ tests độc lập (không phụ thuộc vào nhau)
- ✅ Sử dụng pytest.approx() cho float comparisons

### ❌ Don'ts

- ❌ Không có test database queries trong unit tests
- ❌ Không test implementation details
- ❌ Không create side effects (files, etc.)
- ❌ Không viết super long tests

## 📞 Troubleshooting

### ImportError: No module named 'app'

```bash
# Đảm bảo bạn đang ở trong backend folder
cd backend

# Hoặc thêm vào PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:/path/to/backend"
pytest tests/
```

### Test mất lâu

```bash
# Chạy tests in parallel
pytest tests/ -n auto
```

(Cần cài đặt: `pip install pytest-xdist`)

### Fixture not found

```bash
# Đảm bảo __init__.py tồn tại trong mỗi thư mục
# tests/__init__.py
```

---

**Happy Testing! 🎉**
