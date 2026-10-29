from fastapi import FastAPI
from routes.student_routes import router as student_router

app = FastAPI(title="University Student Records API", version="1.0")

app.include_router(student_router)