import os
from os.path import join, dirname, exists
from dotenv import load_dotenv

current_path = dirname(__file__)
cogs_path = join(current_path,"cogs")
dotenv_path = join(current_path,".env")

extentions = ["cogs."+filename[:-3]for filename in os.listdir(cogs_path)if filename.endswith(".py")]

if exists(dotenv_path):
    load_dotenv(dotenv_path)

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")