from pydantic import BaseSettings


class DevConfig(BaseSettings):

    # secret used for signing JWT tokens
    JWT_SECRET: str

    # hash of payload with pow_token must start with {POW_DIFFICULTY} 0 bits
    POW_DIFFICULTY: int

    # db uri like postgres://user:password@host:port/db-name
    DATABASE_URI: str

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = DevConfig()
