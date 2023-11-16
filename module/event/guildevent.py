import nextcord
from nextcord.ext import commands


class OnGuildJoin(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(guild):
        pass


def setup(bot: commands.Bot):
    bot.add_cog(OnGuildJoin(bot))
