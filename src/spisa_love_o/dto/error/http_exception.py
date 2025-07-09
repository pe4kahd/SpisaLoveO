from src.spisa_love_o.dto.base.response import BaseResponse, BaseResponseMeta


class HttpExceptionResponse(
    BaseResponse[dict, BaseResponseMeta]
):
    """
    Ответ на ошибку
    """

    meta: BaseResponseMeta