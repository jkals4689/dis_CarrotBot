import nextcord
from nextcord.ext import commands

class SetLogChannel:
    def __init__(self) -> None:
        pass

    @commands.command()
    def setlc(self):
        pass

    @setlc.error
    def error_setlc(self):
        pass

    

def setup(bot: commands.Bot):
    bot.add_cog()