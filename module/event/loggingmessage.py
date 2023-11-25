from nextcord.ext import commands
from pathlib import Path
from datetime import datetime

import nextcord
import logging


class MessageLogging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        logging.basicConfig(format='[ %(asctime)s ] [ %(levelname)s ] : %(message)s', datefmt="%d/%m/%Y %H:%M:%D")

        path = Path(Path.cwd() / "log" / "message" / f"{message.guild.id}_{message.guild.name}")
        path.mkdir(parents=True, exist_ok=True)
        current_time = datetime.now()
        date = current_time.strftime("%Y.%m.%d")
        time = current_time.strftime("%H:%M:%S")

        with open(str(path / f"{message.channel.id}_{message.channel.name}_chat.txt"), 'a',
                  encoding='utf-8') as logging_file:
            if not message.author.bot:
                logging_file.write(
                    f"[ {date} ] [ {time} ] : [ {message.author.nick} ] << {message.content}\n")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info(
            f"[ {message.guild.name} ] [ {message.channel.name} ] : [ {message.author.name} ] << {message.content}")


def setup(bot: commands.Bot):
    bot.add_cog(MessageLogging(bot))
