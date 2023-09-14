from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_DBNAME: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()
