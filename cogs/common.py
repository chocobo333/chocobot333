from discord.ext import commands

class common:
    def __init__(self,bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["きる"])
    async def kill(self,ctx):
        await ctx.send("logged out")
        await self.bot.logout()

def setup(bot):
    bot.add_cog(common(bot))