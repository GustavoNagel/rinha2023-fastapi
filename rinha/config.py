from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    ENV: str = "development"
    DEBUG: bool = False
    DATABASE_URI: str = ""
    SECRET_KEY: str


settings = Settings()
