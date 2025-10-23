"""
Calculator Logic Module
Chứa toàn bộ logic tính toán (add, subtract, multiply, divide)
"""


def add(a: float, b: float) -> float:
    """
    Cộng hai số.
    
    Args:
        a: Số thứ nhất
        b: Số thứ hai
    
    Returns:
        Kết quả a + b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Trừ hai số.
    
    Args:
        a: Số thứ nhất
        b: Số thứ hai
    
    Returns:
        Kết quả a - b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Nhân hai số.
    
    Args:
        a: Số thứ nhất
        b: Số thứ hai
    
    Returns:
        Kết quả a * b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Chia hai số.
    
    Args:
        a: Số bị chia
        b: Số chia
    
    Returns:
        Kết quả a / b
    
    Raises:
        ValueError: Khi b = 0 (chia cho 0)
    """
    if b == 0:
        raise ValueError("Không thể chia cho 0")
    return a / b
