from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    GROQ_API_KEY: str

    PINECONE_API_KEY: str
    PINECONE_INDEX: str = "codebase-assistant"

    REDIS_URL: str = "redis://localhost:6379"

    DATABASE_URL: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()