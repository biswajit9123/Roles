import discord
import asyncio
import os
from discord.ext.commands import Bot
from discord.ext import commands

client = Bot(description="poko", command_prefix="*", pm_help = False)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+'')
	print('--------')
	print('--------')
	print('Started <Poko>') 
	return await client.change_presence(game=discord.Game(name='<Roles>')) 



@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='★彡-Guest-彡★')
    await client.add_roles(member, role)
    
    
    
client.run(os.getenv('Token'))
