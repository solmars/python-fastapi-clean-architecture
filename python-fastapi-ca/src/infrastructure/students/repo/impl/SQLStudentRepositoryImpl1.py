
from typing import Union

from inject import autoparams
from infrastructure.students.repo.StudentRepository import StudentRepository
from loaders.database import DatabaseProvider
from models.student.StudentModel import StudentModel, SQLStudentSchema, UpdateStudentModel
from sqlalchemy import delete

class SQLStudentRepository(StudentRepository):

    @autoparams()
    def __init__(self, provider: DatabaseProvider):
        self.provider = provider

    def get_all(self) -> list[StudentModel]:
        session = self.provider.getSQL_db_session()
        allStudents = session.query(SQLStudentSchema).all()
        return list(map(StudentModel.from_orm, allStudents))

    def create(self, student: StudentModel) -> StudentModel:
        session = self.provider.getSQL_db_session()
        persistenceStudent = SQLStudentSchema(
            name=student["name"], course=student["course"], gpa=student["gpa"], email=student["email"])
        session.add(persistenceStudent)
        session.commit()
        session.refresh(persistenceStudent)
        stM = StudentModel.from_orm(persistenceStudent)
        return dict(stM)

    def get_one(self, id: Union[str, int]):
        session = self.provider.getSQL_db_session()
        student = session.query(SQLStudentSchema).get(id)
        return student

    def delete(self, id):
        session = self.provider.getSQL_db_session()
        sql = delete(SQLStudentSchema).where(SQLStudentSchema.id == id)
        session.execute(sql)
        session.commit()

        return True


    def update(self, id, student: UpdateStudentModel):
        # implement logic of update in sql
        pass
