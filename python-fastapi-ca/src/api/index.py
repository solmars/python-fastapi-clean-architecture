

import fastapi

import api.routes.StudentRoute as StudentRoute


def defineRoutes(app: fastapi.FastAPI):
    app.include_router(StudentRoute.router)
