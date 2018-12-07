import discord
import asyncio
import os 
import random
import colorsys
from discord.ext.commands import Bot

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
    print("In our server" + member.name + " just joined")
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Welcome message')
    embed.add_field(name = '__Welcome to Our Server__',value ='**Hope you will be active here. Check Our server rules and never try to break any rules. ',inline = False)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    await client.send_message(member,embed=embed)
    
client.run(os.getenv('Token'))
