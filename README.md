# FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python. It is built on standard Python type hints and is designed for speed, simplicity, and automatic API documentation.

## Installation

1. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

2. Install FastAPI and an ASGI server like Uvicorn:
   ```bash
   pip install fastapi uvicorn
   ```

   Run FastAPI Program:
   python -m uvicorn fileName:app --reload

3. Verify the installation:
   ```bash
   python -c "import fastapi; print(fastapi.__version__)"
   ```

## Brief Overview of FastAPI

- High performance and lightweight
- Easy to create REST APIs
- Automatic request validation and data parsing
- Built-in Swagger UI and ReDoc documentation
- Supports async functions
- Great for modern web services and microservices

## Simple Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

Run the application with:

```bash
uvicorn main:app --reload
```

Then visit:

```text
http://127.0.0.1:8000/docs
```
