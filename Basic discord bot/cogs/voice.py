import discord
import nacl
from discord.ext import commands,tasks
import os
import youtube_dl
import asyncio

class voice(commands.Cog):
  
  def __init__(self, client):
    self.client = client
      
  @commands.command(aliases=["entrar","entre"])
  async def _entrar(self, ctx):
    canal = ctx.author.voice
    if str(canal) == "None":
      await ctx.channel.send("Você precisa estar em um canal!")
    else:
      canal = ctx.author.voice.channel
      await canal.connect()
      
  @commands.command(aliases=["sair","saia"])
  async def _sair(self, ctx):
    
    canal = ctx.author.voice.channel
    if str(canal) == "None":
      await ctx.channel.send("Você precisa estar em um canal!")
    else:
      canal = ctx.guild.voice_client
      await canal.disconnect()

  @commands.command(aliases=["tocar","toque","play"])
  async def stream(self, ctx, *, url):

    async with ctx.typing():
      player = await YTDLSource.from_url(url, loop=self.client.loop, stream=True)
      ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
    await ctx.send(f'Now playing: {player.title}')

  
def setup(client):
  client.add_cog(voice(client))
  