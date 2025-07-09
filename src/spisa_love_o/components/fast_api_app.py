from dependency_injector.wiring import Provide
from fastapi.responses import JSONResponse
from fastapi import Request, HTTPException, FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from src.spisa_love_o.components.database.relation.async_database import AsyncDatabaseRelational
from src.spisa_love_o.components.injectable import injectable
from src.spisa_love_o.components.mixins.logger import LoggerMixin
from src.spisa_love_o.components.routers.base import BaseRouter


@injectable()
class FastApiApp(LoggerMixin):
    def __init__(
        self,
        db: AsyncDatabaseRelational = Provide["database"],
        routers: list[BaseRouter] = Provide["routers"],
        middlewares: list[BaseHTTPMiddleware] = Provide["middlewares"],
        app: FastAPI = Provide['app']
    ):
        self._db = db
        self._app = app
        self.__include_routers(routers)
        self.__add_middlewares(middlewares)
        self.__add_exception_handlers()

    @property
    def app(self) -> FastAPI:
        return self._app

    def __include_routers(self, routers: list[BaseRouter]):
        for router in routers:
            self._app.include_router(router.router, tags=[router.__class__.__name__])

    def __add_middlewares(self, middlewares: list[BaseHTTPMiddleware]):
        for middleware in middlewares:
            self._app.add_middleware(middleware)

    def __add_exception_handlers(self):
        @self._app.exception_handler(HTTPException)
        async def http_exception_handler(request: Request, exc: HTTPException):
            return JSONResponse({
                "payload": {},
                "meta": {
                    "status": "ERROR",
                    "code": f"{exc.status_code}",
                    "messages": [{"name": "Error", "content": exc.detail}]
                }
            }, exc.status_code)