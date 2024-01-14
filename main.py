import os
import time
import nextcord
from nextcord import Guild

import module.event.guildevent as guild_event
import module.event.loggingmessage as log_message

from nextcord.ext import commands
from module.datamodule.checkdatafile import CheckData
from module.datamodule.userdatawriter import GuildInUsersDataWriter

client = commands.Bot(command_prefix=".!", intents=nextcord.Intents.all())
game = nextcord.Game("악악. 살려줘 악악.")


def init():
    """Code boxes that are executed at the start of a program.:return:"""
    # OnMemberEvent.setup(client)
    guild_event.setup(client)
    log_message.setup(client)


def main():
    """
    Program Start Function
    :return:
    """

    @client.event
    async def on_ready():
        await client.change_presence(activity=game)

        guilds: list[Guild] = client.guilds
        for guild in guilds:
            CheckData(guild)
            for member in guild.members:
                GuildInUsersDataWriter(guild).add_userdata(member)

        time.sleep(1)
        print("Online!")

    @client.event
    async def on_close():
        time.sleep(1)
        print("Offline")


if __name__ == "__main__":
    init()
    main()
    client.run(os.environ['CarrotBotToken'])
