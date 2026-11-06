from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI ML Gateway"
    VERSION: str = "1.1.0"
    API_V1_PREFIX: str = "/api/v1"
    
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    CACHE_TTL_SECONDS: int = 3600
    
    DEFAULT_MODEL: str = "llama-3-70b-instruct"
    MAX_TOKENS_LIMIT: int = 4096
    TEMPERATURE_DEFAULT: float = 0.7

    class Config:
        env_file = ".env"

settings = Settings()
