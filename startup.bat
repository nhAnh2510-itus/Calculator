@echo off
REM Script chạy Calculator App Locally (Windows)

echo.
echo ================================================
echo   Calculator - Local Startup (Windows)
echo ================================================
echo.

REM Kiểm tra Docker
docker --version >nul 2>&1
if errorlevel 1 (
    echo [Option 1] Docker không tìm thấy, chạy không Docker
    echo.
    echo [Option 2] Nếu muốn Docker Compose, hãy cài Docker Desktop
    echo.
    
    REM Chạy mà không Docker
    echo Khởi động Backend...
    start cmd /k "cd backend && venv\Scripts\activate && uvicorn app.main:app --reload"
    
    timeout /t 3
    
    echo Khởi động Frontend...
    start cmd /k "cd frontend && python -m http.server 8080"
    
    echo.
    echo ✓ Ứng dụng đã khởi động!
    echo.
    echo 📍 Frontend: http://localhost:8080
    echo 📍 Backend: http://localhost:8000
    echo 📍 API Docs: http://localhost:8000/docs
    echo.
) else (
    echo [1] Docker đã cài đặt
    echo [2] Khởi động với Docker Compose...
    echo.
    
    docker-compose up
    
    echo.
    echo ✓ Ứng dụng đã khởi động!
    echo.
    echo 📍 Frontend: http://localhost:80
    echo 📍 Backend: http://localhost:8000
    echo 📍 API Docs: http://localhost:8000/docs
    echo.
)

pause
