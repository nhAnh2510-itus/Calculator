# 🔧 Python Environment Configuration - Updated

## ✅ Cấu hình đã được cập nhật

Tất cả scripts và files đã được cập nhật để sử dụng `python3` khi tạo virtual environment.

---

## 📋 Quy trình

### **Bước 1: Tạo Virtual Environment (dùng python3)**

```bash
python3 -m venv venv
```

### **Bước 2: Kích hoạt Virtual Environment**

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

### **Bước 3: Các lệnh khác chạy `python` bình thường**

Sau khi kích hoạt venv, mọi lệnh sẽ sử dụng Python từ venv:

```bash
# Tất cả những lệnh này sẽ dùng python từ venv (tự động)
pip install -r requirements.txt
pytest tests/ -v
python app.py
```

**Lưu ý:** Bạn không cần gõ `python3` nữa, chỉ gõ `python` là đủ!

---

## 📝 Files Đã Cập Nhật

### **1. run_tests.bat (Windows)**
- ✅ Sử dụng `python3 -m venv venv`
- ✅ Các lệnh khác dùng `pip` bình thường

### **2. run_tests.sh (Unix/Linux)**
- ✅ Đã sử dụng `python3 -m venv venv` từ trước
- ✅ Hoạt động đúng

### **3. startup.bat (Windows)**
- ✅ Tạo venv bằng `python3`
- ✅ Kích hoạt venv
- ✅ Cài dependencies
- ✅ Chạy backend

### **4. startup.sh (Unix/Linux)**
- ✅ Đã sử dụng `python3` từ trước
- ✅ Hoạt động đúng

### **5. Jenkinsfile**
- ✅ Sử dụng `python3 -m venv venv`
- ✅ Các bước tiếp theo dùng venv tự động

---

## 🚀 Cách Sử Dụng

### **Chạy Tests (Windows)**

```powershell
cd c:\Users\admin\calculator
.\run_tests.bat
```

Hoặc chạy thủ công:

```powershell
cd backend
python3 -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest tests/ -v
```

### **Chạy Tests (macOS/Linux)**

```bash
cd calculator
bash run_tests.sh
```

Hoặc chạy thủ công:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

### **Khởi Động App (Windows)**

```powershell
cd c:\Users\admin\calculator
.\startup.bat
```

### **Khởi Động App (macOS/Linux)**

```bash
cd calculator
bash startup.sh
```

---

## ✨ Lợi Ích của Cách Làm Này

✅ **Rõ ràng:** `python3` cho việc tạo venv  
✅ **Tiêu chuẩn:** Tuân theo best practices  
✅ **Thống nhất:** Hoạt động giống nhau trên tất cả OS  
✅ **Dễ bảo trì:** Dễ thay đổi Python version nếu cần  

---

## 🔍 Kiểm Tra

Sau khi kích hoạt venv, kiểm tra:

```bash
# Xem Python version đang sử dụng
python --version

# Xem Python executable path
python -c "import sys; print(sys.executable)"
```

Output sẽ trỏ đến `venv` folder:
```
C:\Users\admin\calculator\backend\venv\Scripts\python.exe
```

---

## 📌 Tóm Tắt

| Bước | Command |
|------|---------|
| **1. Tạo venv** | `python3 -m venv venv` |
| **2. Kích hoạt** | `source venv/bin/activate` hoặc `.\venv\Scripts\Activate.ps1` |
| **3. Cài deps** | `pip install -r requirements.txt` |
| **4. Chạy tests** | `pytest tests/ -v` |

**Lưu ý:** Sau bước 2, các command khác tự động sử dụng Python từ venv!

---

**Happy Coding! 🚀**
