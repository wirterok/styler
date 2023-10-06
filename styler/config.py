from pydantic import BaseSettings

class Config(BaseSettings):
    ENVIRONMENT: str = "local"

    POSTGRES_HOST: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASS: str = "postgres"
    POSTGRES_DB: str = "styler"
    POSTGRES_PORT: int = 5432

    @property
    def alchemy_host(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASS}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

config = Config(_env_file=".env")