import discord
import random
from discord.ext import commands

class diversao(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["prever"])
  async def _prever(self, ctx, *,pergunta):
    respostas = ["Com certeza",
                 "Provavelmente sim",
                 "Talvez",
                 "Provavelmente não",
                 "Com certeza não"]
    await ctx.send("Pergunta: {} \nResposta: {}".format(pergunta,random.choice(respostas)))
    
def setup(client):
  client.add_cog(diversao(client))