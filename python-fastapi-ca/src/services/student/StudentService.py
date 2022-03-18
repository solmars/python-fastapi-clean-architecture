import inject
from models.student.StudentModel import StudentModel, UpdateStudentModel
from infrastructure.students.repo.StudentRepository import StudentRepository


class StudentService:

    @inject.autoparams()
    def __init__(self, repo: StudentRepository):
        self.repo = repo

    def get_all_students(self):
        return self.repo.get_all()

    def create_student(self, student: StudentModel):
        return self.repo.create(student)

    def get_student(self,id:str):
        return self.repo.get_one(id)

    def update_student(self,id,student:UpdateStudentModel):
        return self.repo.update(id,student)

    def delete_student(self,id):
        return self.repo.delete(id)
        

