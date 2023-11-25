import logging

import nextcord
import shutil

from nextcord.ext import commands
from module.datamodule.checkdatafile import CheckData
from module.datamodule.userdatawriter import GuildDataWriter
from pathlib import Path


class _Message_print:
    def __init__(self, event: str, guild: nextcord.Guild = None, before: nextcord.abc.GuildChannel = None,
                 after: nextcord.abc.GuildChannel = None):
        self.__guild = guild
        self.__before = before
        self.__after = after
        self.__event = event[0].upper() + event[1:]

    def print_join(self):
        print("=" * 10 + f"[ {self.__event} ]" + "=" * 10)
        print(f"Guild Name: {self.__guild.name}\nGuild ID: {self.__guild.id}")
        print("=" * 10 + f"[ {self.__event} ]" + "=" * 10)

    def print_left(self):
        print("=" * 10 + f"[ Guild {self.__event} ]" + "=" * 10)
        print(f"Guild Name: {self.__guild.name}\nGuild ID: {self.__guild.id}")
        print("=" * 10 + f"[ Guild {self.__event} ]" + "=" * 10)

    def print_guild_update(self):
        print("=" * 10 + f"[ Guild {self.__event} ]" + "=" * 10)
        print(f"Before Guild Name: {self.__before.name}\nGuild ID: {self.__before.id}")
        print(f"After Guild Name: {self.__after.name}\nGuild ID: {self.__after.id}")
        print("=" * 10 + f"[ Guild {self.__event} ]" + "=" * 10)

    def print_channel_update(self):
        print("=" * 10 + f"[ Channel {self.__event} ]" + "=" * 10)
        print(f"Guild : {self.__guild.id}_{self.__guild.name}")
        print(f'Before Channel Name: {self.__before.name}\nGuild ID: {self.__before.id}')
        print(f"After Channel Name: {self.__after.name}\nGuild ID: {self.__after.id}")
        print("=" * 10 + f"[ Channel {self.__event} ]" + "=" * 10)

    def __del__(self):
        pass


class OnGuildEvents(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: nextcord.Guild):
        CheckData(guild)
        GuildDataWriter(guild).add_userdata()

        _Message_print("join", guild=guild).print_join()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: nextcord.Guild):
        path = Path(Path.cwd() / "database" / f"{guild.id}_{guild.name}")
        shutil.rmtree(path, ignore_errors=True)

        _Message_print("leave", guild=guild).print_left()


class OnGuildUpdates:
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        logging.basicConfig(format='[ %(asctime)s ] [ %(levelname)s ] : %(message)s', datefmt="%d/%m/%Y %H:%M:%D")

        path = Path(Path.cwd() / "database" / f"{before.id}_{before.name}")
        replace_guild_folder = f"{after.id}_{after.name}"
        path.rename(path.parent / replace_guild_folder)

        self.logger.info(f"[ {before.name} ] [ Channel Update ] : {before.name} => {after.name}")
        _Message_print("update", before=before, after=after).print_guild_update()

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        if isinstance(before, nextcord.TextChannel):
            path = Path(
                Path.cwd() / "log" / "message" / f"{before.guild.id}_{before.guild.name}" / f"{before.id}_{before.name}_chat.txt")
            replace_file_name = f"{after.id}_{after.name}_chat.txt"
            path.rename(path.parent / replace_file_name)

            _Message_print("update", before=before, after=after).print_channel_update()

def setup(bot: commands.Bot):
    bot.add_cog(OnGuildEvents(bot))
