import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


bot.load_extension("Mod")

with open("Token.txt", "r") as f:
  bot.run(f.read())