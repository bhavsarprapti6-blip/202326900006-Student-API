from typing import List, Optional
from models.student import StudentCreate, StudentUpdate

class StudentController:
    def __init__(self):
        self.students: List[dict] = []
        self.counter: int = 0

    def create_student(self, student: StudentCreate) -> dict:
        self.counter += 1
        new_student = {
            "id": self.counter,
            "name": student.name,
            "email": student.email,
            "course": student.course,
            "semester": student.semester
        }
        self.students.append(new_student)
        return new_student

    def get_all_students(self) -> List[dict]:
        return self.students

    def get_student_by_id(self, student_id: int) -> Optional[dict]:
        for student in self.students:
            if student["id"] == student_id:
                return student
        return None

    def update_student(self, student_id: int, student_update: StudentUpdate) -> Optional[dict]:
        for student in self.students:
            if student["id"] == student_id:
                update_data = student_update.model_dump(exclude_unset=True)
                student.update(update_data)
                return student
        return None

    def delete_student(self, student_id: int) -> bool:
        for index, student in enumerate(self.students):
            if student["id"] == student_id:
                self.students.pop(index)
                return True
        return False

student_controller = StudentController()