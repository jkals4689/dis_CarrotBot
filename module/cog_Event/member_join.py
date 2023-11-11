from module.DataWriter import CsvWriter
import nextcord
from nextcord.ext import commands

header = ["Date", "Time", "Member-ID", "Member-Name", "Stat"]


def print_event(string, member):
    print("{} to Member".format(string))
    print("ID[{}]\nMemberName[{}]\n".format(member.id, member.name))


def write_csv(id: str, name: str, stat: str):
    time = t.now()
    data = list()
    data.append([time.strftime("%Y.%m.%d"),
                time.strftime("%H:%M:%S"), id, name, stat])
    dataframe = pd.DataFrame(data, columns=header)
    dataframe.to_csv("./database/test.csv")
    return dataframe


class MemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(member):
        print_event("Join", member)


class MemberLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(member):
        print_event("Leave", member)
