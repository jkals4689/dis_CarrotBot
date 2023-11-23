import nextcord
import shutil

from nextcord.ext import commands
from module.datamodule.checkdatafile import CheckData
from module.datamodule.userdatawriter import GuildDataWriter
from pathlib import Path

class OnGuildEvents(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: nextcord.Guild):
        CheckData(guild)
        GuildDataWriter(guild).add_userdata()

        print("=" * 10+"[ Guild Join ]"+"="*10)
        print(f"Guild Name: {guild.name}\nGuild ID: {guild.id}")
        print("=" * 10+"[ Guild Join ]"+"="*10)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: nextcord.Guild):
        path = Path(Path.cwd()/"database"/f"{guild.id}_{guild.name}")
        shutil.rmtree(path, ignore_errors=True)

        print("=" * 10+"[ Guild Leave ]"+"="*10)
        print(f"Guild Name: {guild.name}\nGuild ID: {guild.id}")
        print("=" * 10 + "[ Guild Leave ]" + "=" * 10)


def setup(bot: commands.Bot):
    bot.add_cog(OnGuildEvents(bot))
