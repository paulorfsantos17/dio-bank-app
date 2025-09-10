from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    database_url_test: str
    environment: str = "production"
    jwt_token: str 

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }

settings = Settings()