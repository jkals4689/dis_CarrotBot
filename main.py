import time
import os

import nextcord
from nextcord.ext import commands

client = commands.Bot(command_prefix=".!", intents=nextcord.Intents.all())
game = nextcord.Game("악악. 살려줘 악악.")


# def init():
#     client.add_cog(MemberLeave(client))
#     client.add_cog(MemberJoin(client))


def main():
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
    # init()
    main()
    client.run(os.environ['CarrotBotToken'])

    
