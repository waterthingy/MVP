from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Cloud Run!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
