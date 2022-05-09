from data.utils.util import *

class base(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="serverlist")
    async def serverlist(self, ctx):

        serverlist = []

        for guild in self.guilds:
            serverlist.append(f"Name: {guild.name}, ID: {guild.id}\n")

        embed = discord.Embed(title="GUILDLIST",
                              colour=ctx.author.colour)

        fields = [("Servers bot is in", f"{len(serverlist)} guilds I am located in", False),
                  ("GUILDS", f"``serverlist``", False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)


    @Cog.listener()
    async def on_ready(self):
        print('base.py connected')

def setup(bot):
    bot.add_cog(base(bot))