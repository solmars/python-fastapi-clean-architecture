from abc import ABC, abstractmethod, ABCMeta
from typing import Union
from models.student.StudentModel import StudentModel, UpdateStudentModel


class StudentRepository(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all(self) -> list[StudentModel]:
        """Get all students"""
        pass

    @abstractmethod
    def create(self, student: StudentModel) -> StudentModel:
        """Create Student"""
        pass

    @abstractmethod
    def get_one(self, id: Union[str, int]) -> StudentModel:
        """Get (one) Student"""
        pass

    @abstractmethod
    def update(self, id: Union[str, int], student: UpdateStudentModel):
        """Update (one) Student"""
        pass

    @abstractmethod
    def delete(self, id: Union[str, int]) -> bool:
        """Delete (one) Student"""
        pass
