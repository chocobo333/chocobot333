
import settings
import discord
import asyncio

DISCORD_TOKEN = settings.DISCORD_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print("logged in")

@client.event
async def on_message(message):
    if message.content.startswith("/neko"):
        reply = "awewewewe"
        await client.send_message(message.channel,reply)



client.run(DISCORD_TOKEN)