import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="poko Official Bot", command_prefix=commands.when_mentioned_or("*"), pm_help = True)
client.remove_command('help')

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='for *help'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='in '+str(len(client.servers))+' servers'))
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Our BOT')
    print('Created by Poko')
    client.loop.create_task(status_task())

def is_dark(ctx):
    return ctx.message.author.id == "514856260353392660"

@client.event
async def on_message(message):
    channel = client.get_channel('519797154705965058')
    if message.server is None and message.author != client.user:
        await client.send_message(channel, '{} : <@{}> : '.format(message.author.name, message.author.id) + message.content)
    await client.process_commands(message)

async def on_message(message):
    user = message.author
    if message.author.bot:
      return
    if message.content.startswith('>say'):
      return
    else:
      if message.content.startswith('>donate'):
          msg = '**Support us by donating us;** https://www.paypal.me/CocoGT'
          await bot.send_message(message.channel, msg)
          
      if 'Who is your creator <@!24791747004989441>?' in message.content:
          msg = 'Coco#6429 is my creator'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
         
      if 'hi <@!24791747004989441>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
         
      if 'bye <@!24791747004989441>' in message.content:
          msg = 'Bye {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
         
      if 'Bye <@!24791747004989441>' in message.content:
          msg = 'Bye {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
                 
      if 'hello <@!24791747004989441>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
         
      if 'Hi <@!24791747004989441>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
          
      if 'Hello <@!24791747004989441>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
          
      if 'how are you <@!24791747004989441>?' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
         
      if 'How are you <@!24791747004989441>?' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
          
      if 'sup <@!24791747004989441>' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
         
      if 'Sup <@!24791747004989441>' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)         
          
      if 'I am also fine <@!24791747004989441>' in message.content:
          msg = 'Cool! {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)          
         
      if 'i am also fine <@!24791747004989441>' in message.content:
          msg = 'Cool! {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)          
          
      if 'fuck' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **fuck**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
      
      if 'FUCK' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **FUCK**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
        
      if 'asshole' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **asshole**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
        
      if 'ASSHOLE' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **ASSHOLE**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
                
      if 'Fuck' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Fuck**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
        
      if 'porn' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **porn**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await bot.send_message(channel, embed=embed)
        
      if 'idiot' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **idiot**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
        
      if 'Porn' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Porn**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
       
      if 'bitch' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **bitch**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Shortform abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'Bitch' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Bitch**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Shortform abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'pussy' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **pussy**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'Shit' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Shit**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'shit' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **shit**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'Pussy' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Pussy**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'Dick' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Dick**',inline = False)

      if 'dick ' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **dick**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

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
    
@client.command(pass_context = True)
async def meme(ctx):
    choices = ['image":"https://i.redd.it/sh4dy1nhq6y11.png', 'https://img.memecdn.com/english_o_869587.webp', 'https://img.memecdn.com/everybody-knows-muricans-don-amp-039-t-speak-english-the-same-way-mexicans-don-amp-039-t-speak-spanish_c_7233205.webp', 'https://img.memecdn.com/english-reaction-when-they-heard-about-eu_c_6994013.webp', 'https://images3.memedroid.com/images/UPLOADED393/5b0c3ee92799f.jpeg' , 'https://images7.memedroid.com/images/UPLOADED850/5b0c2d7dd6049.jpeg', 'https://images7.memedroid.com/images/UPLOADED905/5b0c30c468fa8.jpeg', 'https://images7.memedroid.com/images/UPLOADED726/5b0c2d4c5f288.jpeg', 'https://images7.memedroid.com/images/UPLOADED936/5b0c2a90adbe7.jpeg', 'https://images7.memedroid.com/images/UPLOADED764/5b0c1e491c669.jpeg', 'https://images3.memedroid.com/images/UPLOADED922/5b0c284b71cd0.jpeg', 'https://images3.memedroid.com/images/UPLOADED207/5b0c265a58cf4.jpeg', 'https://images7.memedroid.com/images/UPLOADED920/5b0c06813741a.jpeg', 'https://images3.memedroid.com/images/UPLOADED46/5a91c871e61f1.jpeg', 'https://images7.memedroid.com/images/UPLOADED737/5a91c7f234bd2.jpeg', 'https://images7.memedroid.com/images/UPLOADED757/5a91bd39e1323.jpeg', 'https://images7.memedroid.com/images/UPLOADED963/5a91b4f7aba7e.jpeg', 'https://images7.memedroid.com/images/UPLOADED794/5a91ac0900506.jpeg', 'https://images3.memedroid.com/images/UPLOADED188/5a91aa326ad4e.jpeg']
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title='Meme', description='For more memes check- https://www.memedroid.com', color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/519200090770898945/aca7ea629f7ea397e44284bf474457b8.webp?size=1024') 
    embed.set_image(url = random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context = True)
@commands.check(is_dark)
async def dmall(ctx, *, msg: str):
    for server_member in ctx.message.server.members:
      await client.send_message(server_member, msg)
      await client.delete_message(ctx.message)
    
  
@client.command(pass_context = True)
@commands.check(is_dark)
async def botdm(ctx, user: discord.Member, *, msg: str):
    await client.send_typing(user)
    await client.send_message(user, msg)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if ctx.message.author.bot:
      return
    else:
      if not msg: await client.say("Please specify a message to send")
      else: await client.say(msg)
         
            
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def emojiids(ctx):
  for emoji in ctx.message.author.server.emojis:
    print(f"<:{emoji.name}:{emoji.id}>")
    print(" ")    
			
@client.command(pass_context = True)
async def wow(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:WOW:515854429485006848>')
	
@client.command(pass_context = True)
async def dank(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:OnThaCoco:515853700682743809>')

@client.command(pass_context = True)
async def santa(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:santa:517232271678504970>')
	
@client.command(pass_context = True)
async def hi(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:hi:517232279148429313>')
	
@client.command(pass_context = True)
async def lol(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:lol:517232283670020096>')
	
@client.command(pass_context = True)
async def love(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:love:517232300912672774>')
	
@client.command(pass_context = True)
async def mad(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:mad:517232301176913951>')
	
@client.command(pass_context = True)
async def alien(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:alien:517232332663422986>')

@client.command(pass_context = True)
async def fearfromme(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:shiroeglassespush:516174320532193289>')
	   	
@client.command(pass_context = True)
async def angry(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:angear:516174316950388772>')
	
@client.command(pass_context = True)
async def surprised(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:eyebigger:516174315058626560>')
		
@client.command(pass_context = True)
async def cat(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:agooglecat:516174312294842389>')
		
@client.command(pass_context = True)
async def thinking1(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking:516183328613990400>')
	
@client.command(pass_context = True)
async def thinking2(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking2:516183323127709699>')
	
@client.command(pass_context = True)
async def happy(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:happy:516183323052212236>')
	
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    if userName.server_permissions.kick_members:
        await client.say('**He is mod/admin and i am unable to warn him/her**')
        return
    else:
      await client.send_message(userName, "You have been warned for: **{}**".format(message))
      await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
      pass	
	    
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def dm(ctx, user: discord.Member, *, msg: str):
    try:
        await client.send_message(user, msg)
        await client.delete_message(ctx.message)          
        await client.say("Success! Your DM has made it! :white_check_mark: ")
    except discord.ext.commands.MissingPermissions:
        await client.say("Aw, come on! You thought you could get away with DM'ing people without permissions.")
    except:
        await client.say("Error :x:. Make sure your message is shaped in this way: *dm [tag person] [msg]")

@client.command(pass_context = True)
async def test(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.send_message(ctx.message.author, 'Hii bro what supp')
      await client.say('Check your dm ')	
	
client.run(os.getenv('Token'))
