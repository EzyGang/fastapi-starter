import asyncio

import uvicorn
from fastapi import FastAPI

from app.core.init_app import init_middlewares, lifespan, register_routers
from app.core.logging_config import get_logger
from app.core.settings import get_settings


logger = get_logger(__name__)
config = get_settings()


def create_app() -> FastAPI:
    logger.info('Initializing app...')
    app = FastAPI(title=config.APP_NAME, lifespan=lifespan)
    init_middlewares(app)
    register_routers(app)
    logger.info('App is up and running!')
    return app


if __name__ == '__main__':
    # Local server runner with Uvicorn
    _config = uvicorn.Config(
        app='main:create_app',
        factory=True,
        host=config.HOST,
        port=config.PORT,
        reload=config.AUTO_RELOAD,
        workers=config.WEB_CONCURRENCY,
    )
    server = uvicorn.Server(_config)
    asyncio.run(server.serve())
