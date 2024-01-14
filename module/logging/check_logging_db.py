from pathlib import Path

import nextcord


class CheckLoggingFolder:
    def __init__(self, guild: nextcord.Guild):
        self.path = Path(Path.cwd() / "database" / f"{guild.id}_{guild.name}" / "log")
        self.path.mkdir(parents=True, exist_ok=True)

    def check_message_folder(self, message: nextcord.Message):
        self.path.joinpath("messages",
                           f"{message.channel.id}_{message.channel.name}").mkdir(parents=True, exist_ok=True)
        return self.path

    def __del__(self):
        pass
