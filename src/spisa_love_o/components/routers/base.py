from abc import ABC, abstractmethod
from http import HTTPMethod
from types import FunctionType

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, FastAPI

from src.spisa_love_o.components.injectable import injectable
from src.spisa_love_o.components.mixins.logger import LoggerMixin
from src.spisa_love_o.config import UrlSettings


@injectable()
class BaseRouter(ABC, LoggerMixin):
    _router: APIRouter

    @inject
    def __init__(
        self,
        router: APIRouter = APIRouter(),
        queue_topics: UrlSettings = Provide["settings.provided.url"],
    ):
        self._router = router
        self._queue_topics = queue_topics
        self.__initialize()

    def init_handler(self, handler: FunctionType, method: HTTPMethod, url: str):
        """
        Инициализирует обработчик маршрута FastAPI.

        :param method: HTTP-метод из перечисления HTTPMethod
        :param url: путь маршрута
        :param handler: функция-обработчик
        """

        route_func = {
            HTTPMethod.GET: self._router.get,
            HTTPMethod.POST: self._router.post,
            HTTPMethod.DELETE: self._router.delete,
        }.get(method)

        route_func(url)(handler)
        self._logger.info(f"Handler '{handler.__name__}' initialized on [{method.upper()}] {url}")

    def __initialize(self):
        self._init_routes()
        self._logger.info(f"Router {self.__class__.__name__} initialized")

    @abstractmethod
    def _init_routes(self):
        """
        Привязка эндпоинтов FastAPI к роутеру.
        """
        pass

    @property
    def router(self) -> APIRouter:
        return self._router

    def include_in(self, app: FastAPI):
        """
        Включает роутер в FastAPI приложение.
        """
        app.include_router(self._router)