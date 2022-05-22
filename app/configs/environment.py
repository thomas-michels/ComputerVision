"""
Module to load all Environment variables
"""

from pydantic import BaseSettings


class Environment(BaseSettings):
    """
    Environment, add the variable and its type here matching the .env file
    """
    ACCOUNT_KEY: str
    ENDPOINT: str
    IMGUR_ID: str
    IMGUR_SECRET: str

    class Config:
        """Load config file"""

        env_file = ".env"
