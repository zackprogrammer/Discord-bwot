from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.Listener()
    async def on_ready(self):
        print("To infintie and BEYYYYYYYYYOND")
    @bot.command()
    async def ping(self, ctx):
        await ctx.send('pong')    

def setup(client):
    client.add_cog(Moderation(client))        


