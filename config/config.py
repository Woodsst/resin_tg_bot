from functools import lru_cache

from pydantic import BaseSettings, Field


class Config(BaseSettings):
    token: str = Field("6290030549:AAF9pOX40vz4bW6NfkZKL3nki8X74YtdpTA")


@lru_cache
def get_settings():
    return Config()
