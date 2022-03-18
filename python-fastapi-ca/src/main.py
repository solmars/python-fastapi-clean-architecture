import json
import logging
from fastapi import FastAPI
import uvicorn
from loaders.bootstrap import load



def configure_routing(app) -> None:
    from api.index import defineRoutes
    # NB: I couldn't find a satisfactory way to implement class based routes,
    # so we have to import only on the method so that the injector has already been created
    # this means that this method should only be called after dependencies have been injected.
    defineRoutes(app)


def readConfig() -> json:
    config_file = open('src/config.json')
    return json.load(config_file)


def runApp() -> None:
    # uvicorn.Config.should_reload= configs["reload"]
    configs = readConfig()
    logging.basicConfig(level=logging.DEBUG)
    uvicorn.run(app, port=configs['port'], host=configs['host'])


def configure_all():
    load()
    configure_routing(app)


if __name__ == "__main__":
    app: FastAPI = FastAPI()
    print("Running...")
    configure_all()
    runApp()
