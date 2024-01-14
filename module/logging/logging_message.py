from datetime import datetime

import nextcord
import logging

from nextcord.ext import commands

from module.logging.check_logging_db import CheckLoggingFolder


class MessageLogging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        path = CheckLoggingFolder(message.guild).check_message_folder(message)
        logging.basicConfig(format='[ %(asctime)s ] [ %(levelname)s ] : %(message)s', datefmt="%d/%m/%Y %H:%M:%D")

        current_time = datetime.now()
        date = current_time.strftime("%Y-%m-%d")
        time = current_time.strftime("%H:%M:%S")

        with open(str(path / f"{date}.txt"), 'a', encoding='utf-8') as logging_file:
            if not message.author.bot:
                logging_file.write(
                    f"[ {date} ] [ {time} ] : [ {message.author.name} ] << {message.content}\n")


def setup(bot: commands.Bot):
    bot.add_cog(MessageLogging(bot))
