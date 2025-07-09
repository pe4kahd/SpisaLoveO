from typing import Optional

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core.core_schema import ValidationInfo

class UrlSettings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow",
        env_prefix="SLO__URL"
    )

class AppSettings(BaseSettings):
    name: str = "SLO - SpisaLoveO"
    log_level: str = "DEBUG"
    dev_mode: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="SLO__APP_",
        extra="allow",
    )

class DatabaseRelationalSettings(BaseSettings):
    host: str
    port: str
    name: str
    user: str
    password: str
    url: Optional[str] = None

    @field_validator("url", mode="before")
    @classmethod
    def assemble_url(cls, v: Optional[str], info: ValidationInfo) -> str:
        if isinstance(v, str):
            return v

        data = info.data
        return f"postgresql+asyncpg://{data['user']}:{data['password']}@{data['host']}:{data['port']}/{data['name']}"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow",
        env_prefix="SLO__DB_"
    )


class Settings(BaseSettings):
    url: UrlSettings = UrlSettings()
    app: AppSettings = AppSettings()
    database: DatabaseRelationalSettings = DatabaseRelationalSettings()

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow",
        env_prefix="SLO__"
    )