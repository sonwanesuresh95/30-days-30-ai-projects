from pydantic import BaseSettings

class Settings(BaseSettings):
    model_name: str = "llama3:8b"
    ollama_host: str = "localhost"
    ollama_port: int = 11434
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
