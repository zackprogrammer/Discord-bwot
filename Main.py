import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

with open("Token.txt", "r") as f:
  bot.run(f.read())