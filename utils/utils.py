import sys
from os import path
from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__name__))


def load_env_file():
    """Get the current operating system and activate the correct env file."""
    load_dotenv(path.join(base_dir, '.env'))
