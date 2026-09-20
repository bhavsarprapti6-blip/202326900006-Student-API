from fastapi import FastAPI
from routes.student_routes import router as student_router

app = FastAPI(title="University Student Management API", version="1.0.0")

app.include_router(student_router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the University Student Records API"}