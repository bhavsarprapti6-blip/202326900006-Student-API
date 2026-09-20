from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class StudentBase(BaseModel):
    name: str
    email: EmailStr
    course: str
    semester: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    course: Optional[str] = None
    semester: Optional[int] = None

class StudentResponse(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)