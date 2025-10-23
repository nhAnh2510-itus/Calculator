#!/bin/bash
# Script chạy Calculator App Locally (macOS/Linux)

echo ""
echo "================================================"
echo "  Calculator - Local Startup (Unix/Linux)"
echo "================================================"
echo ""

# Kiểm tra Docker
if ! command -v docker &> /dev/null; then
    echo "[Option 1] Docker không tìm thấy, chạy không Docker"
    echo ""
    echo "[Option 2] Nếu muốn Docker Compose, hãy cài Docker"
    echo ""
    
    # Chạy mà không Docker
    echo "Khởi động Backend (Terminal 1)..."
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    echo "Chạy: uvicorn app.main:app --reload"
    uvicorn app.main:app --reload &
    BE_PID=$!
    
    sleep 3
    
    # Terminal 2
    echo ""
    echo "Khởi động Frontend (Terminal 2)..."
    cd ../frontend
    echo "Chạy: python -m http.server 8080"
    python -m http.server 8080 &
    FE_PID=$!
    
    echo ""
    echo "✓ Ứng dụng đã khởi động!"
    echo ""
    echo "📍 Frontend: http://localhost:8080"
    echo "📍 Backend: http://localhost:8000"
    echo "📍 API Docs: http://localhost:8000/docs"
    echo ""
    echo "PIDs: Backend=$BE_PID, Frontend=$FE_PID"
    echo "Nhấn Ctrl+C để dừng cả hai"
    
    wait
else
    echo "[1] Docker đã cài đặt"
    echo "[2] Khởi động với Docker Compose..."
    echo ""
    
    docker-compose up
    
    echo ""
    echo "✓ Ứng dụng đã khởi động!"
    echo ""
    echo "📍 Frontend: http://localhost:80"
    echo "📍 Backend: http://localhost:8000"
    echo "📍 API Docs: http://localhost:8000/docs"
    echo ""
fi
