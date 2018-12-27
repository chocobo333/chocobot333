
import settings
import asyncio
import discord

DISCORD_TOKEN = settings.DISCORD_TOKEN

class BotClient(discord.Client):
    async def on_ready(self):
        print("logged in")
        print(self.user.name)
        print(self.user.id)

    async def on_message(self,message):
        if message.content.startswith("/neko"):
            await message.channel.send("awewewewe")

client = BotClient()
client.run(DISCORD_TOKEN)