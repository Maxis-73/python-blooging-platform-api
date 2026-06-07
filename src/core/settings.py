from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Info
    PROJECT_NAME: str = "Blogging Platform API"
    PROJECT_DESCRIPTION: str = "API for manage blog posts"
    PROJECT_VERSION: str = "1.0.0"

    # Database
    DB_URI: str

    class Config:
        env_file = ".env"

settings = Settings()