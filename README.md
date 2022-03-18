# python-fastapi-clean-architecture

This project was done in preparation for the implementation of a REST api with python & FastAPI with certain requirements, it is a blueprint for following clean/onion architecture.

Due to its architecture, it supports various adaptations of databases through dependency injection, as an example, there is both MongoDB and SQL implementations present in the project, easily altered by changing a line in src/config.json


Main technologies:

- FastAPI
- SQLAlchemy
- pymongo
- pydantic
- inject (dependency injection library https://github.com/ivankorobkov/python-inject)