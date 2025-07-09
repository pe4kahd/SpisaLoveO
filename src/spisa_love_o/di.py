from logging import Handler, StreamHandler

from dependency_injector import containers, providers
from dependency_injector.providers import Factory, List, Singleton
from fastapi import FastAPI

from src.spisa_love_o.components.middlewares.error import ErrorHandlingMiddleware
from src.spisa_love_o.config import Settings
from src.spisa_love_o.components.log import create_log_handler, get_logger


class DependencyInjector(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["src.spisa_love_o"])

    settings = Singleton(Settings)

    formatted_stream_handler: Factory[Handler] = Factory(
        create_log_handler,
        handler=Factory(StreamHandler),
        name=providers.Callable(lambda s: s.app.name, settings),
        level=providers.Callable(lambda s: s.app.log_level, settings),
    )

    logger_handlers = List(
        formatted_stream_handler,
    )

    logger = Factory(
        get_logger,
        name=providers.Callable(lambda s: s.app.name, settings),
        level=providers.Callable(lambda s: s.app.log_level, settings),
        handlers=logger_handlers,
    )

    routers = List()

    middlewares = List(
        ErrorHandlingMiddleware
    )

    app = Singleton(
        FastAPI,
        title=providers.Callable(lambda s: s.app.name, settings),
        docs_url="/"
    )
