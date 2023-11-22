import nextcord
from nextcord.ext import commands
from module.datamodule.checkdatafile import CheckData
from module.datamodule.datawriter import DataWriter


class OnGuildJoin(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild:nextcord.Guild):
        CheckData(guild)
        data_write = DataWriter(guild)
        for member in guild.members:
            data_write.add_userdata(member)

        print(f"Join to [{guild.name}]Server!\nGuild ID: {guild.id}")
        
def setup(bot: commands.Bot):
    bot.add_cog(OnGuildJoin(bot))
