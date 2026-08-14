from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

# Base schema shared properties
class EmployeeBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    phone_number: str = Field(..., min_length=7, max_length=20)
    department: str = Field(..., min_length=2, max_length=50)
    designation: str = Field(..., min_length=2, max_length=50)
    salary: float = Field(..., gt=0)

# Properties to receive on creation
class EmployeeCreate(EmployeeBase):
    pass

# Properties to receive on update (all optional)
class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    salary: Optional[float] = None

# Properties to return to client (includes id and timestamp)
class EmployeeResponse(EmployeeBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True