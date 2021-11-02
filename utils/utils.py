import sys
from os import path
from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__name__))


def load_env_file():
    """Get the current operating system and activate the correct env file."""
    if sys.platform == 'linux' or sys.platform == 'linux2':
        load_dotenv(path.join(base_dir, '.unix.env'))
    elif sys.platform == 'win32':
        load_dotenv(path.join(base_dir, '.windows.env'))
    else:
        load_dotenv(path.join(base_dir, '.macos.env'))
