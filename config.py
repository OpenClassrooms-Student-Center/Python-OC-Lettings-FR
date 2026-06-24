"""
Config module for environment variables
"""
import os

from dotenv import load_dotenv


load_dotenv()

SENTRY_KEY = os.getenv("SENTRY_KEY")
