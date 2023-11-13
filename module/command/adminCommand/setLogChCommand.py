import nextcord
from nextcord.ext import commands
from module.DataWriter import CsvWriter

class SetLogChannel(commands.Cog):
    def __init__(self, guild, bot:commands.Bot) -> None:
        self.bot = bot
        self.__guild = guild

    @commands.command()
    def setlc(self, ctx, channel: nextcord.TextChannel = None):
        pass

    @setlc.error
    def error_setlc(self):
        pass

    

def setup(bot: commands.Bot):
    bot.add_cog()