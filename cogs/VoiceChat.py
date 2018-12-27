import discord
from discord.ext import commands
import pyttsx

class VoiceChat:
    def __init__(self,bot):
        self.bot: commands.Bot = bot
        self.tts_member_list = list()

    @commands.group(aliases=["ててす"])
    async def tts(self,ctx):
        if ctx.invoked_subcommand is None:
            raise commands.BadArgument()

    @tts.command(aliases=["s"])
    async def start(self, ctx):
        self.tts_member_list.append(ctx.message.author)
        await ctx.send("@{} tts started".format(ctx.message.author.name))

    async def on_message_delete(self,message):
        await message.channel.send("message deleted")

def setup(bot):
    bot.add_cog(VoiceChat(bot))