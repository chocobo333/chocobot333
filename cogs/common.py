from discord.ext import commands

class common:
    def __init__(self,bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["きる"])
    async def kill(self,ctx):
        await ctx.("logged out")
        await self.bot.logout()

    @commands.command()
    async def test(self,ctx):
        await ctx.send("testestestest")

def setup(bot):
    bot.add_cog(common(bot))