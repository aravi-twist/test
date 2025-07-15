# If you see import errors, run: pip install fastapi uvicorn pydantic
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from .calculator import (
    add, subtract, multiply, divide, sin, cos, tan, convert_currency, get_currency_list
)

app = FastAPI()

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BasicOpRequest(BaseModel):
    a: float
    b: float
    op: str  # 'add', 'subtract', 'multiply', 'divide'

class TrigRequest(BaseModel):
    angle: float
    func: str  # 'sin', 'cos', 'tan'
    degrees: Optional[bool] = False

class FXRequest(BaseModel):
    amount: float
    from_currency: str
    to_currency: str

@app.post("/api/basic")
def basic_op(req: BasicOpRequest):
    try:
        if req.op == 'add':
            return {"result": add(req.a, req.b)}
        elif req.op == 'subtract':
            return {"result": subtract(req.a, req.b)}
        elif req.op == 'multiply':
            return {"result": multiply(req.a, req.b)}
        elif req.op == 'divide':
            return {"result": divide(req.a, req.b)}
        else:
            raise HTTPException(status_code=400, detail="Invalid operation")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/trig")
def trig_op(req: TrigRequest):
    try:
        degrees = bool(req.degrees)
        if req.func == 'sin':
            return {"result": sin(req.angle, degrees=degrees)}
        elif req.func == 'cos':
            return {"result": cos(req.angle, degrees=degrees)}
        elif req.func == 'tan':
            return {"result": tan(req.angle, degrees=degrees)}
        else:
            raise HTTPException(status_code=400, detail="Invalid trig function")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/fx")
def fx_op(req: FXRequest):
    try:
        result = convert_currency(req.amount, req.from_currency, req.to_currency)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/currencies")
def currencies():
    return {"currencies": get_currency_list()} 