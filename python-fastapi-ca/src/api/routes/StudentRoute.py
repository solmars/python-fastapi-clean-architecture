import logging
from typing import List

import inject
from controllers.student.StudentController import StudentController
from models.student.StudentModel import StudentModel, UpdateStudentModel
from fastapi import Body, HTTPException, status, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter(prefix="/v1/students")

studentController = inject.get_injector().get_instance(StudentController)


@router.get("/", response_description="List all students", response_model=List[StudentModel])
async def list_students():
    logging.debug('Calling list_students GET endpoint')
    return studentController.get_all_students()


@router.post("/", response_description="Add new student", response_model=StudentModel)
async def create_student(student: StudentModel = Body(...)):
    logging.info('Calling create_student POST endpoint')
    student = jsonable_encoder(student)
    created_student = studentController.create_student(student)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)


@router.get("/{id}", response_description="Get a single student", response_model=StudentModel)
async def show_student(id: str):
    student = studentController.get_student(id)
    if (student is None):
        raise HTTPException(status_code=404, detail=f"Student {id} not found")
    return student


@router.put("/{id}", response_description="Update a student", response_model=StudentModel)
async def update_student(id: str, student: UpdateStudentModel = Body(...)):
    result = studentController.update_student(id, student)
    if(result is None):
        raise HTTPException(status_code=404, detail=f"Student {id} not found")
    return result


@router.delete("/{id}", response_description="Delete a student")
async def delete_student(id: str):
    if(studentController.delete_student(id)):
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Student {id} not found")
