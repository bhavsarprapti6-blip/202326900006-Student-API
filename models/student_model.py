from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    id: int
    name: str
    email: str
    course: str
    semester: int

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    course: Optional[str] = None
    semester: Optional[int] = None