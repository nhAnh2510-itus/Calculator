#!/bin/bash
# Script chạy tests cho Calculator Backend (macOS/Linux)

echo ""
echo "=========================================="
echo "  Calculator - Test Runner (Unix/Linux)"
echo "=========================================="
echo ""

cd backend

# Kiểm tra nếu venv đã tồn tại
if [ ! -d "venv" ]; then
    echo "[1/4] Tạo Virtual Environment..."
    python3 -m venv venv
    echo "✓ Virtual Environment đã tạo"
else
    echo "[1/4] Virtual Environment đã tồn tại, bỏ qua..."
fi

echo "[2/4] Kích hoạt Virtual Environment..."
source venv/bin/activate

echo "[3/4] Cài đặt dependencies..."
pip install -r requirements.txt -q

echo "[4/4] Chạy tests..."
echo ""
pytest tests/ -v --cov=app --cov-report=html --cov-report=term-missing

echo ""
echo "=========================================="
echo "  ✓ Test hoàn tất!"
echo "=========================================="
echo ""
echo "📊 Coverage Report: htmlcov/index.html"
echo ""
