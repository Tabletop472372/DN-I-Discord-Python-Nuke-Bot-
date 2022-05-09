from data.utils.util import *

import discord
from discord.ext import commands
from discord.ext.commands import Bot as Botbase
from discord.ext.commands import CommandNotFound
from discord.ext.commands import command, has_permissions, bot_has_permissions
from discord.ext.commands import Cog

import asyncio
from glob import glob
import json
import os

from ..db import db

PREFIX = ('>>')

class main(Botbase):
    def __init__(self):
        self.ready = False
        self.prefix = PREFIX
    
        super().__init__(command_prefix=PREFIX,
                        case_insensitive=True,
                        intents=discord.Intents.all())

        for filename in os.listdir("./cog"):
            if filename.endswith(".py"):
                self.load_extension(f"cog.{filename[:-3]}")

    def setup(self):
        pass
    
    def run(self):
        with open("./library/bot/token0", "r", encoding="utf-8") as tokenfile:
            self.TOKEN = tokenfile.read()
    
        super().run(self.TOKEN, reconnect=True)
    
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            print('Bot is ready')
    
        else:
            print('Bot reconnected')
    
    async def on_error(self, err, *args, **kwargs):
        if err == "command_error":
            await args[0].send('Context error occurred')
    
            raise
            
        elif hasattr(exc, "original"):
            raise exc.original
    
        else:
            raise exc
    
    async def on_connect(self):
         print('Bot connected')
    
    async def on_disconnect(self):
        print('Bot disconnected')

    async def status_task(self):
        while True:
            await self.change_presence(activity=discord.Game(name="Overseer Bot"))
            await asyncio.sleep(15)
            await self.change_presence(activity=discord.Game(name="Running version 6.0.7"))
            await asyncio.sleep(15)
            await self.change_presence(activity=discord.Game(name="Command prefix is: '>>'"))
            await asyncio.sleep(15)


bot = main()