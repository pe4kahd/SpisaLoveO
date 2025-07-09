from typing import Generic, Optional, Union, TypeVar

from pydantic import BaseModel, ConfigDict, field_validator

from src.spisa_love_o.components.enums.response_statuses import ResponseStatus


class Message(BaseModel):
    """Сообщение, деталь ответа"""

    name: str
    """Уникальное название сообщения"""
    content: str
    """Сообщение в человекочитаемом формате"""


class BaseResponseMeta(BaseModel):
    """Метаданные сообщения"""

    status: ResponseStatus
    """Статус запроса, OK или ERROR"""
    code: str
    """Код ответа: 200, 400 и т.д."""
    messages: list[Message]
    """Список сообщений"""


class EmptyResponsePayload(BaseModel):
    """Пустой Payload"""

    model_config = ConfigDict(extra="forbid")


ResponsePayload = TypeVar("ResponsePayload", bound=BaseModel)
ResponseMeta = TypeVar("ResponseMeta", bound=BaseModel)


class BaseResponse(BaseModel, Generic[ResponsePayload, ResponseMeta]):
    payload: Optional[Union[ResponsePayload, EmptyResponsePayload]] = None
    meta: ResponseMeta

    @field_validator("payload", mode="after")
    @classmethod
    def convert_empty_payload_to_none(cls, v):
        if isinstance(v, EmptyResponsePayload):
            return None
        return v
