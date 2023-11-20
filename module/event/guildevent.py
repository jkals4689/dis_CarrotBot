import nextcord
from nextcord.ext import commands
from module.datamodule.checkdatafile import CheckData


@commands.Bot.listen()
async def on_guild_join(guild):
    CheckData(guild)
    print("Join to [{}]Server!\nGuild ID: {}".format(guild.name, guild.id))


def setup(bot: commands.Bot):
    bot.add_listener(on_guild_join())
