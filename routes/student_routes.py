from fastapi import APIRouter, status
from models.student_model import Student, StudentUpdate
from controllers import student_controller

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    return student_controller.create_student(student)

@router.get("/", status_code=status.HTTP_200_OK)
def read_all_students():
    return student_controller.get_all_students()

@router.get("/{id}", status_code=status.HTTP_200_OK)
def read_student(id: int):
    return student_controller.get_student_by_id(id)

@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_student(id: int, student_update: StudentUpdate):
    return student_controller.update_student(id, student_update)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id: int):
    return student_controller.delete_student(id)