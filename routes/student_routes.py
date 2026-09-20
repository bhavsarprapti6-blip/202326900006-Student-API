from fastapi import APIRouter, HTTPException, status
from typing import List
from models.student import StudentCreate, StudentUpdate, StudentResponse
from controllers.student_controller import student_controller

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    """Create a new student record"""
    return student_controller.create_student(student)

@router.get("/", response_model=List[StudentResponse], status_code=status.HTTP_200_OK)
def get_all_students():
    """Retrieve all student records"""
    return student_controller.get_all_students()

@router.get("/{student_id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def get_student_by_id(student_id: int):
    """Retrieve a single student record by ID"""
    student = student_controller.get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{student_id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def update_student(student_id: int, student_update: StudentUpdate):
    """Update an existing student record"""
    updated_student = student_controller.update_student(student_id, student_update)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    """Delete a student record"""
    success = student_controller.delete_student(student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return None