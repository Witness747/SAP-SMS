from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str

    SECRET_KEY: str

    FRONTEND_URL: str = "http://localhost:5173"

    APP_NAME: str = "SAP-SMS API"

    APP_VERSION: str = "1.0.0"


    class Config:
        env_file = ".env"


settings = Settings()