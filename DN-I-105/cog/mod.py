from data.utils.util import *

class mod(Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @has_permissions(manage_guild=True)
    @command(name="mute", aliases=["supress"])
    async def mutemember(self, ctx, targets: Greedy[Member], *, reason: Optional[str] = "N/A"):
      guild = ctx.guild

      mutedrole = discord.utils.get(guild.roles, name = "muted")

      if not mutedrole:
        mutedrole = await guild.create_role(name = "muted")

        for channel in guild.channels:
          await channel.set_permissions(mutedrole, speak=False, send_messages=False, read_message_history=False)

      if not len(targets):
        await ctx.send(f"``MISSING ARGUMENT``")

      else:
        unmutes = []

        for target in targets:
          if (ctx.guild.me.top_role.position > target.top_role.position):

            if target.id == ctx.message.author.id:
              await ctx.send(f"``YOU CANNOT MUTE YOURSELF``")
              return

            await target.send(f"``MUTED IN {guild.name} FOR:``{reason}``")

            await target.edit(roles=[mutedrole])

            embed = discord.Embed(title=f"``{target.name} MUTED``",
                                    colour=target.colour)

            embed.set_thumbnail(url=ctx.author.avatar_url)

            fields = [("VICTIM", target.display_name, False),
                      ("COMMIT BY", ctx.author.display_name, False),
                      ("REASON", reason, False)]

            for name, value, inline in fields:
              embed.add_field(name=name, value=value, inline=inline)

            await ctx.send(embed=embed)

          else:
            embed = discord.Embed(title=f"{target.display_name} COULD NOT BE MUTED",
                                  colour=target.colour)

            embed.set_thumbnail(url=ctx.author.avatar_url)

            await ctx.send(embed=embed)

        await ctx.send(f"``PROCESS COMPLETE``")
        
    @has_permissions(manage_guild=True)
    @command(name="unmute", aliases=["unsupress"])
    async def unmutemember(self, ctx, targets: Greedy[Member]):
      guild = ctx.guild

      mutedrole = discord.utils.get(guild.roles, name = "muted")

      if not len(targets):
        await ctx.send(f"``MISSING ARGUMENT``")
        return

      else:
        for target in targets:

          await target.send(f"``UNMUTED FROM {guild.name} FOR:``")
          
          await target.remove_roles(mutedrole)

          embed = discord.Embed(title=f"{target.name} UNMUTED",
                                colour=target.colour)

          embed.set_thumbnail(url=ctx.author.avatar_url)

          fields = [("VICTIM", target.display_name, False),
                    ("COMMIT BY", ctx.author.display_name, False)]

          for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

          await ctx.send(embed=embed)
          
    @has_permissions(manage_guild=True)
    @command(name="kick")
    async def kickmember(self, ctx, targets: Greedy[Member], *, reason: Optional[str] = "N/A"):
      guild = ctx.guild

      if not len(targets):
        await ctx.send(f"``MISSING ARGUMENT``")
        return

      for target in targets:
        if (ctx.guild.me.top_role.position > target.top_role.position):

          if target.id == ctx.message.author.id:
            await ctx.send(f"``YOU CANNOT KICK YOURSELF``")
            return

          await target.send(f"``KICKED FROM {guild.name} FOR:``",
                            f"```{reason}```")

          await target.kick(reason=reason)

          embed = discord.Embed(title=f"``{target.name} KICKED``",
                                    colour=target.colour)

          embed.set_thumbnail(url=ctx.author.avatar_url)

          fields = [("VICTIM", target.display_name, False),
                    ("COMMIT BY", ctx.author.display_name, False),
                    ("REASON", reason, False)]

          for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

          await ctx.send(embed=embed)
          
        else:
          embed = discord.Embed(title=f"{target.display_name} COULD NOT BE KICKED",
                                colour=target.colour)

          embed.set_thumbnail(url=ctx.author.avatar_url)

          await ctx.send(embed=embed)

      await ctx.send(f"``PROCESS COMPLETE``")
      
    @has_permissions(manage_guild=True)
    @command(name="ban")
    async def banmember(self, ctx, targets: Greedy[Member], reason: Optional[str] = "N/A"):
      guild = ctx.guild

      if not len(targets):
        await ctx.send(f"``MISSING ARGUMENT``")
        return

      for target in targets:
        if (ctx.guild.me.top_role.position > target.top_role.position):

          if target.id == ctx.message.author.id:
            await ctx.send(f"``YOU CANNOT BANISH YOURSELF``")
            return

          await target.send(f"``BANISHED FROM {guild.name} FOR:``",
                            f"```{reason}```")

          await target.ban(reason=reason)

          embed = discord.Embed(title=f"``{target.name} BANISHED``",
                                    colour=target.colour)

          embed.set_thumbnail(url=ctx.author.avatar_url)

          fields = [("VICTIM", target.display_name, False),
                    ("COMMIT BY", ctx.author.display_name, False),
                    ("REASON", reason, False)]

          for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

          await ctx.send(embed=embed)
          
        else:
          embed = discord.Embed(title=f"{target.display_name} COULD NOT BE BANNED",
                                colour=target.colour)

          embed.set_thumbnail(url=ctx.author.avatar_url)

          await ctx.send(embed=embed)

      await ctx.send(f"``PROCESS COMPLETE``")
      
    @has_permissions(manage_guild=True)
    @command(name="unban")
    async def unbanmember(self, ctx, targets: Greedy[Member]):
      guild = ctx.guild
      
      if not len(targets):
        await ctx.send(f"``MISSING ARGUMENT``")
        return

      for target in targets:

        if target.id == ctx.message.author.id:
          await ctx.send(f"``YOU ARE NOT BANNED?``")
          return

        await target.unban()

        embed = discord.Embed(title=f"``{target.name} BANISHED``",
                              colour=target.colour)

        embed.set_thumbnail(url=ctx.author.avatar_url)

        fields = [("VICTIM", target.display_name, False),
                  ("COMMIT BY", ctx.author.display_name, False),
                  ("REASON", reason, False)]

        for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

      await ctx.send(f"``PROCESS COMPLETE``")

    @Cog.listener()
    async def on_ready(self):
        print('mod.py connected')

def setup(bot):
    bot.add_cog(mod(bot))
