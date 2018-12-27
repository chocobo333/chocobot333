
import settings
import asyncio
import discord
from discord.ext import commands
import traceback

DISCORD_TOKEN = settings.DISCORD_TOKEN

extentions = settings.extentions

class BotClient(commands.Bot):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        for cog in extentions:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    async def on_ready(self):
        print("logged in")
        print(self.user.name)
        print(self.user.id)

    async def on_message(self,message):
        if message.author.bot:
            return

        if message.content.startswith("/neko"):
            await message.channel.send("awewewewe")

        await self.process_commands(message)


client = BotClient(command_prefix="!")
client.run(DISCORD_TOKEN)