/**
 * Calculator Frontend - JavaScript
 * Xử lý giao diện và gọi Backend API
 */

// Địa chỉ Backend (điều chỉnh theo cần thiết)
const BACKEND_URL = 'http://localhost:8000';

// Biến lưu trữ trạng thái
let display = '0';
let previousValue = null;
let operation = null;
let shouldResetDisplay = false;

// Lấy các phần tử DOM
const displayElement = document.getElementById('display');
const statusElement = document.getElementById('status');

/**
 * Cập nhật màn hình hiển thị
 */
function updateDisplay() {
    displayElement.value = display;
}

/**
 * Xóa tất cả
 */
function clearDisplay() {
    display = '0';
    previousValue = null;
    operation = null;
    shouldResetDisplay = false;
    clearStatus();
    updateDisplay();
}

/**
 * Xóa ký tự cuối cùng
 */
function deleteLast() {
    if (display.length > 1) {
        display = display.slice(0, -1);
    } else {
        display = '0';
    }
    updateDisplay();
}

/**
 * Thêm số vào display
 */
function appendNumber(num) {
    if (shouldResetDisplay) {
        display = num;
        shouldResetDisplay = false;
    } else {
        if (display === '0' && num !== '.') {
            display = num;
        } else if (num === '.' && display.includes('.')) {
            return; // Không cho phép nhiều dấu chấm
        } else {
            display += num;
        }
    }
    clearStatus();
    updateDisplay();
}

/**
 * Thêm operator
 */
function appendOperator(op) {
    if (operation !== null) {
        // Nếu đã có operation, thực hiện tính toán trước
        calculate();
    }
    
    previousValue = parseFloat(display);
    operation = op;
    shouldResetDisplay = true;
    clearStatus();
}

/**
 * Gọi Backend API để tính toán
 */
async function calculateWithAPI(a, b, op) {
    try {
        const endpoint = getEndpoint(op);
        
        const response = await fetch(`${BACKEND_URL}${endpoint}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ a, b }),
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Lỗi từ Server');
        }
        
        const data = await response.json();
        return data.result;
    } catch (error) {
        showError(error.message);
        return null;
    }
}

/**
 * Lấy endpoint dựa vào operator
 */
function getEndpoint(op) {
    const endpoints = {
        '+': '/add',
        '-': '/subtract',
        '*': '/multiply',
        '/': '/divide',
    };
    return endpoints[op] || '/add';
}

/**
 * Tính toán
 */
async function calculate() {
    if (operation === null || previousValue === null) {
        return;
    }
    
    const currentValue = parseFloat(display);
    
    // Gọi Backend API
    const result = await calculateWithAPI(previousValue, currentValue, operation);
    
    if (result !== null) {
        // Định dạng kết quả (không hiển thị quá nhiều số lẻ)
        display = result.toString();
        
        // Nếu kết quả có quá nhiều số lẻ, làm tròn
        if (display.includes('.')) {
            const parts = display.split('.');
            if (parts[1].length > 10) {
                display = parseFloat(display).toFixed(10).toString();
                display = display.replace(/\.?0+$/, ''); // Xóa trailing zeros
            }
        }
        
        previousValue = null;
        operation = null;
        shouldResetDisplay = true;
        showSuccess(`${previousValue} ${operation} ${currentValue} = ${display}`);
    }
    
    updateDisplay();
}

/**
 * Hiển thị lỗi
 */
function showError(message) {
    statusElement.style.color = '#ff4757';
    statusElement.textContent = `❌ Lỗi: ${message}`;
}

/**
 * Hiển thị thành công
 */
function showSuccess(message) {
    statusElement.style.color = '#26de81';
    statusElement.textContent = `✓ Tính toán thành công`;
}

/**
 * Xóa status message
 */
function clearStatus() {
    statusElement.textContent = '';
}

/**
 * Khởi tạo
 */
function init() {
    updateDisplay();
    console.log('Calculator App initialized');
    console.log(`Backend URL: ${BACKEND_URL}`);
}

// Gọi init khi trang được load
window.addEventListener('load', init);

// Hỗ trợ phím tắt trên keyboard
document.addEventListener('keydown', (event) => {
    const key = event.key;
    
    if (key >= '0' && key <= '9') {
        appendNumber(key);
    } else if (key === '.') {
        appendNumber('.');
    } else if (key === '+' || key === '-') {
        appendOperator(key);
    } else if (key === '*') {
        event.preventDefault();
        appendOperator('*');
    } else if (key === '/') {
        event.preventDefault();
        appendOperator('/');
    } else if (key === 'Enter' || key === '=') {
        event.preventDefault();
        calculate();
    } else if (key === 'Backspace') {
        event.preventDefault();
        deleteLast();
    } else if (key === 'Escape') {
        event.preventDefault();
        clearDisplay();
    }
});
