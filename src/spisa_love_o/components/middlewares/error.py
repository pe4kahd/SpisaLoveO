from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from src.spisa_love_o.components.enums.response_statuses import ResponseStatus
from src.spisa_love_o.components.exceptions.abstract import AbstractApplicationException
from src.spisa_love_o.dto.base.response import BaseResponseMeta, Message
from src.spisa_love_o.dto.error.http_exception import HttpExceptionResponse


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)

        except AbstractApplicationException as exc:
            meta = BaseResponseMeta(status=ResponseStatus.ERROR, code=exc.code, messages=[Message(name="error", content=str(exc))])
            return JSONResponse(
                status_code=401,
                content=HttpExceptionResponse(payload={}, meta=meta).model_dump()
            )

        except Exception as exc:
            meta = BaseResponseMeta(status=ResponseStatus.ERROR, code="500", messages=[Message(name="error", content=str(exc))])
            return JSONResponse(
                status_code=500,
                content=HttpExceptionResponse(payload={},meta=meta).model_dump()
            )