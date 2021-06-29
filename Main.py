import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def load(ctx, extension):
    bot.load_extensions(f'cogs.{extensions[:-3]}')  


@bot.command()      


async def unload(ctx, extension):
    bot.unload_extensions(f'cogs.{extensions}')



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extensions(f'cogs.{filename}')

with open("Token.txt", "r") as f:
  bot.run(f.read())