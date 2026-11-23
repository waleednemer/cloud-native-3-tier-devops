
from fastapi import FastAPI  # noqa: I001

from app.routers.employee import router as employee_router


app = FastAPI(
    title="Employee Management System",
    description="A Cloud Native 3-Tier DevOps Project",
    version="1.0.0",
)


app.include_router(employee_router)


@app.get("/")
def root():
    return {
        "message": "Employee Management System API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
