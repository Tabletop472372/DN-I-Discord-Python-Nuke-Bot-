from data.utils.util import *

class base(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="base")
    async def base(self, ctx):
        await ctx.send("base")

    @command(name="log1")
    async def mbase(self, ctx):
        await ctx.send("base: response? (y/n)")

        while True:
            try:
                def check_data(message):
                    return message.author == ctx.message.author
                    
                msg = await self.bot.wait_for('message', check=check_data, timeout=tm)
                
                if msg.content == "yes" or "y":
                    await ctx.send(ym)

                    rn = datetime.now()

                    f = open('./data/mallogs.txt', "a")
                    f.write(f"""
=> LOG1 COMMAND PROCESS RUN <=
Time: {rn.strftime("%H:%M:%s")}, {rn.strftime("%D:%M:%Y")}
Actioned by: {ctx.message.author.id} ({ctx.message.author.name}#{ctx.message.author.discriminator})
Server executed in: {ctx.guild.name}
Server id: {ctx.guild.id}
                           """)
                    f.close()

                elif msg.content == "no" or "n":
                    await ctx.send(nm)
                    break

                else:
                    await ctx.send(nam)
                    break

            except:
                pass

    @Cog.listener()
    async def on_ready(self):
        print('base.py connected')

def setup(bot):
    bot.add_cog(base(bot))