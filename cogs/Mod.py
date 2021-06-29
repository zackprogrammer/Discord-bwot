from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.Listener()
    async def on_ready(self):
        print("To infintie and BEYYYYYYYYYOND")
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')    
    @commands.command()
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        if not reason:
            await user.kick("User has been kicked of no reason")
        else:
            await user.kick(reason=reason)
            await ctx.send(f"User got gnomed out of the server for {reason}. And you are a lunatic for doing that") 

def setup(client):
    client.add_cog(Moderation(client))        


