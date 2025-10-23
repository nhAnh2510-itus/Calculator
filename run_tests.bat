@echo off
REM Script chạy tests cho Calculator Backend (Windows)

echo.
echo ==========================================
echo   Calculator - Test Runner (Windows)
echo ==========================================
echo.

cd backend

REM Kiểm tra nếu venv đã tồn tại
if not exist "venv\" (
    echo [1/4] Tạo Virtual Environment...
    python -m venv venv
    echo ✓ Virtual Environment đã tạo
) else (
    echo [1/4] Virtual Environment đã tồn tại, bỏ qua...
)

echo [2/4] Kích hoạt Virtual Environment...
call venv\Scripts\activate

echo [3/4] Cài đặt dependencies...
pip install -r requirements.txt -q

echo [4/4] Chạy tests...
echo.
pytest tests/ -v --cov=app --cov-report=html --cov-report=term-missing

echo.
echo ==========================================
echo   ✓ Test hoàn tất!
echo ==========================================
echo.
echo 📊 Coverage Report: htmlcov/index.html
echo.
pause
