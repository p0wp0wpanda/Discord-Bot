import os
import time

#import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='marco')
async def marco_polo(ctx):
    response = 'Polo!'
    await ctx.send(response)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(error)

@bot.command(name='terminate', help='Logs the bot out of discord (admin permissions required)')
@commands.has_role('admin')
async def terminate(ctx):
    response = 'Bye!'
    await ctx.send(response)
    
    await bot.logout()

bot.run(TOKEN)

# client = discord.Client()

# @client.event
# async def on_ready():
#     guild = discord.utils.get(client.guilds, name=GUILD)
    
#     print (
#         f'{client.user} connected to the following guilds :\n'
#         f'{guild.name}(id: {guild.id})'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')


# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     print(f'{message.author} just sent a message at {message.created_at} in {message.guild}')
    
#     if message.content == '!marco':
#         response = 'Polo!'
#         await message.channel.send(response)

#     elif message.content == '!terminate':
#         await client.logout()

#     elif message.content == '!kys':
#         response = 'This bot will self destruct in'
#         await message.channel.send(response)

#         for i in range(5,0,-1):
#             await message.channel.send(str(i))
#             time.sleep(1)

#         await client.logout()

#     elif message.content == 'raise-exception':
#         raise discord.DiscordException
    
# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise

# client.run(TOKEN)
