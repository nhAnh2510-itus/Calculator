"""
Unit Tests cho app/logic.py
Kiểm tra toàn bộ logic tính toán
"""

import pytest
from app.logic import add, subtract, multiply, divide


class TestAdd:
    """Test các trường hợp của hàm add"""
    
    def test_add_positive_numbers(self):
        """Test cộng hai số dương"""
        assert add(5, 3) == 8
    
    def test_add_negative_numbers(self):
        """Test cộng hai số âm"""
        assert add(-5, -3) == -8
    
    def test_add_mixed_numbers(self):
        """Test cộng số âm và số dương"""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
    
    def test_add_with_zero(self):
        """Test cộng với 0"""
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(0, 0) == 0
    
    def test_add_float_numbers(self):
        """Test cộng số thực"""
        assert add(5.5, 3.2) == pytest.approx(8.7)


class TestSubtract:
    """Test các trường hợp của hàm subtract"""
    
    def test_subtract_positive_numbers(self):
        """Test trừ hai số dương"""
        assert subtract(5, 3) == 2
    
    def test_subtract_negative_numbers(self):
        """Test trừ hai số âm"""
        assert subtract(-5, -3) == -2
    
    def test_subtract_mixed_numbers(self):
        """Test trừ số âm và số dương"""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8
    
    def test_subtract_with_zero(self):
        """Test trừ với 0"""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0
    
    def test_subtract_float_numbers(self):
        """Test trừ số thực"""
        assert subtract(5.5, 3.2) == pytest.approx(2.3)


class TestMultiply:
    """Test các trường hợp của hàm multiply"""
    
    def test_multiply_positive_numbers(self):
        """Test nhân hai số dương"""
        assert multiply(5, 3) == 15
    
    def test_multiply_negative_numbers(self):
        """Test nhân hai số âm"""
        assert multiply(-5, -3) == 15
    
    def test_multiply_mixed_numbers(self):
        """Test nhân số âm và số dương"""
        assert multiply(5, -3) == -15
        assert multiply(-5, 3) == -15
    
    def test_multiply_by_zero(self):
        """Test nhân với 0"""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0
    
    def test_multiply_float_numbers(self):
        """Test nhân số thực"""
        assert multiply(5.5, 2) == pytest.approx(11.0)


class TestDivide:
    """Test các trường hợp của hàm divide"""
    
    def test_divide_positive_numbers(self):
        """Test chia hai số dương"""
        assert divide(10, 2) == 5
    
    def test_divide_negative_numbers(self):
        """Test chia hai số âm"""
        assert divide(-10, -2) == 5
    
    def test_divide_mixed_numbers(self):
        """Test chia số âm và số dương"""
        assert divide(10, -2) == -5
        assert divide(-10, 2) == -5
    
    def test_divide_float_numbers(self):
        """Test chia số thực"""
        assert divide(10.0, 2.5) == pytest.approx(4.0)
    
    def test_divide_by_zero(self):
        """Test chia cho 0 - phải throw ValueError"""
        with pytest.raises(ValueError, match="Không thể chia cho 0"):
            divide(10, 0)
    
    def test_divide_zero_by_number(self):
        """Test chia 0 cho số khác"""
        assert divide(0, 5) == 0
