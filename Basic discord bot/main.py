import discord
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.command()
async def load(ctx, extensao):
  client.load_extension("cogs.{}".format(extensao))
  await ctx.send("Cog {} carregada!".format(extensao))
  
@client.command()
async def unload(ctx, extensao):
 client.unload_extension("cogs.{}".format(extensao)) 
 await ctx.send("Cog {} descarregada!".format(extensao))

@client.command()
async def reload(ctx, extensao):
 client.unload_extension("cogs.{}".format(extensao)) 
 client.load_extension("cogs.{}".format(extensao))
 await ctx.send("Cog {} recarregada!".format(extensao))
  
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    client.load_extension("cogs.{}".format(filename[:-3]))
  
client.run(os.environ["token"])
