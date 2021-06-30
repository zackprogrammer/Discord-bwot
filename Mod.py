from discord.ext import commands
from discord import Message
import discord

class MyCog(commands.Cog):  # All cogs must inherit from commands.Cog
    """A simple, basic cog."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Bans user
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
      await member.ban(reason=reason)
      await ctx.send(f'User {member} has been Gnomed out of the server.')


    #  Unbans user
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split("#")

      for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return  
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kick')            




def setup(bot: commands.Bot):
    bot.add_cog(MyCog(bot))