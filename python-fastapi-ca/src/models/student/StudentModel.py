from typing import Optional, Union
from pydantic import BaseModel, EmailStr, Field
from models.shared.PyObjectId import PyObjectId
from bson import ObjectId

from sqlalchemy import Column, Integer, String,Sequence,Float

from loaders.database import Base

class SQLStudentSchema(Base):
    __tablename__ = 'users'
    id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    email = Column(String)
    course = Column(String)
    gpa = Column(Float)

#works as model, dto and as validator of request, in this case it can work as DTO without a problem but should be separated in case it cannot.
class StudentModel(BaseModel):
    id: Union[int,PyObjectId] = Field(default_factory=PyObjectId,alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
    gpa: float = Field(..., le=4.0)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        orm_mode=True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "course": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
            }
        }


class UpdateStudentModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    course: Optional[str]
    gpa: Optional[float]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "course": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
            }
        }
