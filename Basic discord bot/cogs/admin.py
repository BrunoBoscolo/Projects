import discord
from discord.ext import commands

class administrador(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["chutar"])
  async def kick(self, ctx, membro: discord.Member, *, razao=None):
    await membro.kick(reason=razao)
  
  @commands.command(aliases=["banir","martelo"])
  async def ban(self, ctx, membro: discord.Member, *, razao=None):
    await membro.ban(reason=razao)
  
  @commands.command(aliases=["limpar,limpe"])
  async def limpar(self, ctx, quantidade=5):
    await ctx.channel.purge(limit=quantidade)
    
  @commands.command(aliases=["cargo"])
  async def _cargo(self, ctx, *, ncargo, cor):
    guild = ctx.guild
    cor=int(cor)
    await guild.create_role(name=ncargo, color=discord.Colour(cor))
  
  @commands.command(aliases=["tag"])
  async def _tag(self, ctx, membro: discord.Member, *, cargo):
    cargo = discord.utils.get(ctx.guild.roles, name=cargo)
    await membro.add_roles(membro,cargo)

  @commands.command(aliases=["bot_jogo"])
  async def _status(self, ctx, *, jogo): 
    await self.client.change_presence(status=discord.Status.online,activity=discord.Game(jogo))
    await ctx.send("Mudando o jogo do bot para: {}".format(jogo))
    
def setup(client):
  client.add_cog(administrador(client))