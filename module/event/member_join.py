from module.DataWriter import CsvWriter
import nextcord
from nextcord.ext import commands


def print_event(string, member):
    print()
    print("{} to Member".format(string))
    print("ID[{}]\nMemberName[{}]\n".format(member.id, member.name))


class MemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        data = CsvWriter(f"{member.guild.id}_{member.guild.name}", 'jl')
        data.add_data(member.id, member.name, 'Join')
        data.save_file()
        print_event("Join", member)


class MemberLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        data = CsvWriter(f"{member.guild.id}_{member.guild.name}", 'jl')
        data.add_data(member.id, member.name, 'Leave')
        data.save_file()
        print_event("Leave", member)
