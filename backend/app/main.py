"""
Calculator FastAPI Application
Cung cấp các API endpoint cho calculator
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.logic import add, subtract, multiply, divide

app = FastAPI(title="Calculator API", version="1.0.0")

# Cấu hình CORS để cho phép Frontend gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả origin (để demo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CalculationRequest(BaseModel):
    """Model cho request"""
    a: float
    b: float


class CalculationResponse(BaseModel):
    """Model cho response"""
    result: float


class ErrorResponse(BaseModel):
    """Model cho error response"""
    detail: str


@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Calculator API is running"}


@app.post("/add", response_model=CalculationResponse)
def api_add(request: CalculationRequest):
    """API để cộng hai số"""
    result = add(request.a, request.b)
    return CalculationResponse(result=result)


@app.post("/subtract", response_model=CalculationResponse)
def api_subtract(request: CalculationRequest):
    """API để trừ hai số"""
    result = subtract(request.a, request.b)
    return CalculationResponse(result=result)


@app.post("/multiply", response_model=CalculationResponse)
def api_multiply(request: CalculationRequest):
    """API để nhân hai số"""
    result = multiply(request.a, request.b)
    return CalculationResponse(result=result)


@app.post("/divide", response_model=CalculationResponse)
def api_divide(request: CalculationRequest):
    """API để chia hai số"""
    try:
        result = divide(request.a, request.b)
        return CalculationResponse(result=result)
    except ValueError as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=str(e))
