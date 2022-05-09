from data.utils.util import *

class ginfo(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command("userinfo")
    async def userinfo(self, ctx, targets: Greedy[Member]):

        rolelist = []

        embed = discord.Embed(title=f"``USERINFO``",
                            colour=ctx.author.colour)

        if not len(targets):

            for role in ctx.author.roles:
                rolelist.append(role.mention)

                embed.set_thumbnail(url=ctx.author.avatar_url)

                fields = [(f"User ID", f"``{ctx.author.id}``", False),
                          (f" Account registered at", f"``{ctx.author.created_at}``", False),
                          (f"Joined guild at", f"``{ctx.author.joined_at}``", False),
                          (f"Roles", f"{rolelist}", False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await ctx.send(embed=embed)

                return

        for target in targets:
        
            for role in target.roles:
                rolelist.append(role.mention)

            embed.set_thumbnail(url=target.avatar_url)

            fields = [(f"User ID", f"``{target.id}``", False),
                      (f" Account registered at", f"``{target.created_at}``", False),
                      (f"Joined guild at", f"``{target.joined_at}``", False),
                      (f"Roles", f"{rolelist}", False)]
    
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
    
            await ctx.send(embed=embed)

    @command(name="guildinfo")
    async def guildinfo(self, ctx):
        guild=ctx.guild
    
        embed = discord.Embed(title="GUILDINFO",
                                colour=ctx.author.colour)
    
        embed.set_thumbnail(url=guild.icon_url)
    
        fields = [(f"Owner", f"``ID: {guild.owner_id}``", False),
                 (f"Guild created at", f"``{guild.created_at}``", False),
                 (f"Member Count", f"``{len(guild.members)} Members``", False),
                 (f"Role Count", f"``{len(list(guild.roles))}``", False),
                 (f"Channel Count", f"``{len(list(guild.channels))}``", False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
    
        await ctx.send(embed=embed)

    @command("av", aliases=["avatar"])
    async def avatar(self, ctx, targets: Greedy[Member]):

        embed = discord.Embed(title=f"``AVATAR``",
                              colour=ctx.author.colour)

        if not len(targets):
            embed.set_image(url=ctx.author.avatar_url)

        for target in targets:
            embed.set_image(url=target.avatar_url)

        await ctx.send(embed=embed)

    @command(name="guildicon", aliases=["icon"])
    async def icon(self, ctx):
        
        embed = discord.Embed(title=f"``GUILD ICON``",
                              colour=ctx.author.colour)

        embed.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        print('ginfo.py connected')

def setup(bot):
    bot.add_cog(ginfo(bot))