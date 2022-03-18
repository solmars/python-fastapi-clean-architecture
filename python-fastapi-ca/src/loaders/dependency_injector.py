from h11 import Data
import inject
from controllers.student.StudentController import StudentController
from infrastructure.students.repo.StudentRepository import StudentRepository
from loaders.database import DatabaseProvider
from services.student.StudentService import StudentService
from pydoc import locate
import json


def getConfig():
    config = open('src/config.json')
    return json.load(config)


def configure_injection(binder):
    databaseProvider = DatabaseProvider()
    binder.bind(DatabaseProvider, databaseProvider)

    # we only load repo from config file, could easily be done for controller and services aswell
    configJson = getConfig()
    studentRepoPath = configJson["students"]["repo"]
    studentRepositoryClass = locate(studentRepoPath)

    studentRepositoryInstance = studentRepositoryClass(databaseProvider)
    studentService = StudentService(studentRepositoryInstance)
    studentController = StudentController(studentService)

    # NB: as far as I could see, the inject library had the best syntax out of all DI libraries, but doesn't seem to allow for (Type,Type) Binding
    # IE: (StudentRepository,StudentRepositoryImpl) like microsoft EF so we have to bind by instance.
    binder.bind(StudentController, studentController)
    binder.bind(StudentService, studentService)
    binder.bind(StudentRepository, studentRepositoryClass)


def performInjection():
    inject.configure(configure_injection)
