from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Configuration

from .application import make_fastapi_app
from .config import config


class Container(DeclarativeContainer):
    config = Configuration()
    fastapi_app = Factory(make_fastapi_app)


def bootstap() -> Container:
    container = Container()
    container.config.from_pydantic(config)
    return container
