from typing import Union
from inject import autoparams
from loaders.database import DatabaseProvider

from models.student.StudentModel import StudentModel, UpdateStudentModel
from infrastructure.students.repo.StudentRepository import StudentRepository


class MongoDBStudentRepository(StudentRepository):

    @autoparams()
    def __init__(self, provider: DatabaseProvider):
        self.dbTable = provider.getMongo_DB()["students"]

    # all of the following should be dtos on return
    def get_all(self) -> list[StudentModel]:
        students = self.dbTable.find()
        return list(students)

    def create(self, student: StudentModel) -> StudentModel:
        new_student = self.dbTable.insert_one(student)
        created_student = self.dbTable.find_one(
            {"_id": new_student.inserted_id})
        return created_student

    def get_one(self, id: Union[str, int]):
        return self.dbTable.find_one({"_id": id})

    def update(self, id, student: UpdateStudentModel):
        student = {k: v for k, v in student.dict().items() if v is not None}
        if len(student) >= 1:
            update_result = self.dbTable.update_one(
                {"_id": id}, {"$set": student})

            if update_result.modified_count == 1:
                if (
                    updated_student := self.dbTable.find_one({"_id": id})
                ) is not None:
                    return updated_student

    def delete(self, id):
        result = self.dbTable.delete_one({"_id": id})
        if result.deleted_count == 0:
            return False
        return True
