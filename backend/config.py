from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pathlib import Path
import os

# Load the .env file from the project root
# env_path = Path(__file__).resolve().parent.parent / ".env"
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    APP_NAME: str = "Blog Project"
    DEBUG: bool = True
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}"

    class Config:
        env_file = ".env"

settings = Settings()