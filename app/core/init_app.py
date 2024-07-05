from collections.abc import Callable

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.apps.routes import api_v1_to_routers_map
from app.core.settings import get_settings


settings = get_settings()


def create_on_startup_handler(app: FastAPI) -> Callable:
    async def on_startup() -> None:
        pass

    return on_startup


def create_on_shutdown_handler(app: FastAPI) -> Callable:
    async def on_shutdown() -> None:
        pass

    return on_shutdown


def init_middlewares(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


def register_routers(app: FastAPI) -> None:
    for api_v, routers in api_v1_to_routers_map.items():
        for router in routers:
            app.include_router(router, prefix=f'{settings.API_PREFIX}/{api_v}')


def register_events(app: FastAPI) -> None:
    app.add_event_handler('startup', create_on_startup_handler(app))
    app.add_event_handler('shutdown', create_on_shutdown_handler(app))
