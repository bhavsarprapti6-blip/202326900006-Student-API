from fastapi import HTTPException, status, Response
from models.student_model import Student, StudentUpdate

fake_db = []

def get_all_students():
    return fake_db

def get_student_by_id(student_id: int):
    for student in fake_db:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

def create_student(student: Student):
    for existing in fake_db:
        if existing["id"] == student.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Student with this ID already exists")
    
    student_dict = student.model_dump()
    fake_db.append(student_dict)
    return student_dict

def update_student(student_id: int, student_update: StudentUpdate):
    for index, student in enumerate(fake_db):
        if student["id"] == student_id:
            update_data = student_update.model_dump(exclude_unset=True)
            fake_db[index].update(update_data)
            return fake_db[index]
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

def delete_student(student_id: int):
    for index, student in enumerate(fake_db):
        if student["id"] == student_id:
            fake_db.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")