
import settings
import asyncio
import discord
from discord.ext import commands
from traceback import print_exc
import re

DISCORD_TOKEN = settings.DISCORD_TOKEN

extentions = settings.extentions

url_only_channel_id = 528091405273268237

url_pattern = "(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)"

class BotClient(commands.Bot):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        for cog in extentions:
            try:
                self.load_extension(cog)
            except Exception:
                print_exc()

        self.unload_extension("cogs.VoiceChat")

    async def on_ready(self):
        print("logged in")
        print(self.user.name)
        print(self.user.id)

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if message.channel.id == url_only_channel_id:
            match = re.match(url_pattern,message.content)
            if not match:
                await message.delete()
                msg = await message.channel.send("In this channel, you are allowed to send only url.")
                await asyncio.sleep(3)
                await msg.delete()
                
        await self.process_commands(message)
    

    # async def on_command_error(self,ctx,error):
    #     await ctx.send(str(error))


client = BotClient(command_prefix="!")
client.run(DISCORD_TOKEN)