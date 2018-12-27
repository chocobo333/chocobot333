
import settings
import asyncio
import discord
from discord.ext import commands
from traceback import print_exc

DISCORD_TOKEN = settings.DISCORD_TOKEN

extentions = settings.extentions

class BotClient(commands.Bot):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        for cog in extentions:
            try:
                self.load_extension(cog)
            except Exception:
                print_exc()

    async def on_ready(self):
        print("logged in")
        print(self.user.name)
        print(self.user.id)

    async def on_message(self,message):
        if message.author.bot:
            return

        await self.process_commands(message)

    # async def on_command_error(self,ctx,error):
    #     await ctx.send(str(error))


client = BotClient(command_prefix="!")
client.run(DISCORD_TOKEN)