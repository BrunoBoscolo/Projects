import discord
from discord.ext import commands

class inicio(commands.Cog):

  def __init__(self, client):
    self.client = client

  #events
  @commands.Cog.listener()
  async def on_ready(self):
    print("Bot está online!")
    await self.client.change_presence(status=discord.Status.online,activity=discord.Game("Dominação Mundial..."))

  #commands
  #@commands.command()
  #async def ping(self, ctx):
  #  await ctx.send("Pong!")
    
def setup(client):
  client.add_cog(inicio(client))