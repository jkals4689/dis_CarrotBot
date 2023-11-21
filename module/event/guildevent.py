import nextcord
from nextcord.ext import commands
from module.datamodule.checkdatafile import CheckData


class OnGuildJoin(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        CheckData(guild)
        print("Join to [{}]Server!\nGuild ID: {}".format(guild.name, guild.id))
        
def setup(bot: commands.Bot):
    bot.add_cog(OnGuildJoin(bot))
