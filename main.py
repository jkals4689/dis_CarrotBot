import os
import time
import nextcord

from nextcord.ext import commands
# from module.event import OnMemberEvent
import module.event.guildevent as guildevent
# from module.datamodule.checkdatafile import check_datafile

client = commands.Bot(command_prefix=".!", intents=nextcord.Intents.all())
game = nextcord.Game("악악. 살려줘 악악.")


def init():
    """Code boxes that are executed at the start of a program.:return:"""
    # OnMemberEvent.setup(client)
    guildevent.setup(client)


def main():
    """
    Program Start Function
    :return:
    """
    @client.event
    async def on_ready():
        await client.change_presence(activity=game)
        print("Carrot Bot is Starting...")
        time.sleep(3)
        print("Online!")

    @client.event
    async def on_close():
        print("Carrot Bot is Shutdown...")
        time.sleep(3)
        print("Offline")


if __name__ == "__main__":
    init()
    main()
    client.run(os.environ['CarrotBotToken'])
