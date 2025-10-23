"""
API Tests cho app/main.py
Kiểm tra các endpoint của FastAPI
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestRootEndpoint:
    """Test root endpoint"""
    
    def test_root_endpoint(self):
        """Test GET /"""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json()["message"] == "Calculator API is running"


class TestAddAPI:
    """Test ADD endpoint"""
    
    def test_add_api_success(self):
        """Test POST /add thành công"""
        response = client.post("/add", json={"a": 5, "b": 3})
        assert response.status_code == 200
        assert response.json()["result"] == 8
    
    def test_add_api_with_negative_numbers(self):
        """Test POST /add với số âm"""
        response = client.post("/add", json={"a": -5, "b": 3})
        assert response.status_code == 200
        assert response.json()["result"] == -2
    
    def test_add_api_with_floats(self):
        """Test POST /add với số thực"""
        response = client.post("/add", json={"a": 5.5, "b": 3.2})
        assert response.status_code == 200
        result = response.json()["result"]
        assert abs(result - 8.7) < 0.01


class TestSubtractAPI:
    """Test SUBTRACT endpoint"""
    
    def test_subtract_api_success(self):
        """Test POST /subtract thành công"""
        response = client.post("/subtract", json={"a": 5, "b": 3})
        assert response.status_code == 200
        assert response.json()["result"] == 2
    
    def test_subtract_api_with_negative_numbers(self):
        """Test POST /subtract với số âm"""
        response = client.post("/subtract", json={"a": 5, "b": -3})
        assert response.status_code == 200
        assert response.json()["result"] == 8


class TestMultiplyAPI:
    """Test MULTIPLY endpoint"""
    
    def test_multiply_api_success(self):
        """Test POST /multiply thành công"""
        response = client.post("/multiply", json={"a": 5, "b": 3})
        assert response.status_code == 200
        assert response.json()["result"] == 15
    
    def test_multiply_api_by_zero(self):
        """Test POST /multiply với 0"""
        response = client.post("/multiply", json={"a": 5, "b": 0})
        assert response.status_code == 200
        assert response.json()["result"] == 0


class TestDivideAPI:
    """Test DIVIDE endpoint"""
    
    def test_divide_api_success(self):
        """Test POST /divide thành công"""
        response = client.post("/divide", json={"a": 10, "b": 2})
        assert response.status_code == 200
        assert response.json()["result"] == 5
    
    def test_divide_api_with_floats(self):
        """Test POST /divide với số thực"""
        response = client.post("/divide", json={"a": 10.0, "b": 2.5})
        assert response.status_code == 200
        result = response.json()["result"]
        assert abs(result - 4.0) < 0.01
    
    def test_divide_api_by_zero(self):
        """Test POST /divide chia cho 0 - phải return lỗi 400"""
        response = client.post("/divide", json={"a": 10, "b": 0})
        assert response.status_code == 400
        assert "Không thể chia cho 0" in response.json()["detail"]
    
    def test_divide_api_zero_by_number(self):
        """Test POST /divide 0 cho số khác"""
        response = client.post("/divide", json={"a": 0, "b": 5})
        assert response.status_code == 200
        assert response.json()["result"] == 0
