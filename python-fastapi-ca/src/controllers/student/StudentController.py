import inject

from models.student.StudentModel import StudentModel, UpdateStudentModel
from services.student.StudentService import StudentService


class StudentController:

    @inject.autoparams()
    def __init__(self, service: StudentService):
        self.service = service

    def get_all_students(self):
        return self.service.get_all_students()

    def create_student(self,student: StudentModel):
        return self.service.create_student(student)

    def get_student(self,id:str):
        return self.service.get_student(id)

    def update_student(self,id:str,student:UpdateStudentModel):
        if self.get_student(id) is None:
            return None
        return self.service.update_student(id,student)

    def delete_student(self,id:str):
        return self.service.delete_student(id)
