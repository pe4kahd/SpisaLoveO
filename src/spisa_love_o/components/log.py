from logging import Handler, StreamHandler, Logger, getLogger
from typing import Literal
from colorlog import ColoredFormatter


LogLevelLiteral = Literal[
    "CRITICAL", "FATAL", "ERROR", "WARN", "WARNING", "INFO", "DEBUG", "NOTSET"
]


def get_logger(
    name: str, level: LogLevelLiteral, handlers: list[Handler] = None
) -> Logger:
    if handlers is None:
        handlers = [create_log_handler(StreamHandler(), name, level)]
    logger = getLogger(name)
    logger.setLevel(level=level)
    for handler in handlers:
        logger.addHandler(handler)
    return logger


def create_log_handler(handler: Handler, name: str, level: LogLevelLiteral) -> Handler:
    formatter = ColoredFormatter(
        f"%(log_color)s{'name'}%(reset)s - [%(name)s] - %(asctime)s - %(log_color)s%(levelname)s%(reset)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )
    handler.setLevel(level.upper())
    handler.setFormatter(formatter)
    return handler