from discord.ext import commands

class common:
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def test(self,ctx):
        await ctx.send("testestestest")

def setup(bot):
    bot.add_cog(common(bot))