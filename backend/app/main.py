from fastapi import FastAPI

app = FastAPI(title="AI Learning Coach API", version="0.1.0")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "AI Learning Coach Backend is running"}

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Learning Coach API"}
