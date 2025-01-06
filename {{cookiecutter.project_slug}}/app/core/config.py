import os
from typing import List
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field


class Config:
    APP_ENV = os.getenv("APP_ENV", "development")

load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "{{ cookiecutter.project_slug }}"
    DATABASE_URL: str = ""
    REDIS_URL: str = ""
    SCHEMAS: str = ""
    SECRET_KEY: str = ""
    ALGORITHM: str = ""

    SLOW_API_THRESHOLD: float = 2
    GLOBAL_RATE_LIMIT: int = 100

    LOGGING_LEVEL: str = "INFO"

    OPENSEARCH_URL: str = ""
    OPENSEARCH_PORT: int = Field(9200, env="OPENSEARCH_PORT")
    OPENSEARCH_SCHEME: str = "https"
    OPENSEARCH_CONECTION_WITH_AWS: bool = Field(
        False, env="OPENSEARCH_CONECTION_WITH_AWS"
    )

    @property
    def schema_list(self) -> List[str]:
        return [s.strip() for s in self.SCHEMAS.split(",")]

    @property
    def schema_list_without_public(self) -> List[str]:
        return [s for s in self.schema_list if s != "public_schema" and s != "public"]

    class ConfigDict:
        env_prefix = "APP_"
        env_file = ".env"


settings = Settings()
