from typing import Callable

from fastapi import FastAPI

from styler.container import bootstap

def run(bootstrap: Callable = bootstap) -> FastAPI:
    app = bootstap().fastapi_app()

    return app
