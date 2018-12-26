import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__),".env")
load_dotenv(dotenv_path)

DISCORD_TOKEN = str(os.environ.get("DISCORD_TOKEN"))