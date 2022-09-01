import discord
import math
from discord.ext import commands

class matematica(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["somar"])
  async def soma(self, ctx, n1, n2):
    soma = str(int(n1)+int(n2))
    await ctx.send("A soma de {} e {} é {}".format(n1,n2,soma))

  @commands.command(aliases=["bhk","bhaskara"])
  async def _bhk(self, ctx, a, b, c):
    
    a = int(a)
    b = int(b)
    c = int(c)
    delta = (b*b)-(4*a*c)
    if delta<0:
      await ctx.send("A raiz é negativa!")
  
    else:
      soma_p = str(((b*-1)+math.sqrt(delta))/2*a)
      soma_n = str(((b*-1)-math.sqrt(delta))/2*a)
      await ctx.send("As raizes para: \nA={}\nB={}\nC={}\nSão:\nX1={}\nX2={}".format(a,b,c,soma_p,soma_n))
  
  @commands.command(aliases=["ptg","pitagoras"])
  async def _pit(self, ctx, ca, co):
    
    ca = int(ca)
    co = int(co)
  
    if(ca>0 and co>0):
      hip = math.sqrt((ca*ca)+(co*co))
      await ctx.send("A hiotenusa vale: {:.2f}".format(hip))
    else:
      await ctx.send("Os valores dos catetos devem ser positivos!")
      
  @commands.command(aliases=["sub","subtrair"])
  async def _sub(self, ctx, n1, n2):
    soma = str(int(n1)-int(n2))
    await ctx.send("A subtração de {} e {} é {}".format(n1,n2,soma))
  
  @commands.command(aliases=["div","dividir"])
  async def _div(self, ctx, n1, n2):
    soma = str(int(n1)/int(n2))
    await ctx.send("A divisão de {} e {} é {}".format(n1,n2,soma))
  
  @commands.command(aliases=["mult","multiplicar"])
  async def _mult(self, ctx, n1, n2):
    soma = str(int(n1)*int(n2))
    await ctx.send("A multiplicação de {} e {} é {}".format(n1,n2,soma))
  
  @commands.command(aliases=["areac"])
  async def _areac(self, ctx, r):
    if(int(r)>0):
      area = (int(r)**2)*3.14159265359
      await ctx.send("a area do circulo de raio: {} é:   {:.2f}m²".format(r, area))
    else:
      await ctx.send("o valor do raio tem que ser positivo!")
      
  @commands.command(aliases=["areaq"])
  async def _areaq(self, ctx, b, h):
    if(int(b)>0 and int(h)>0):
      area = (int(b))*(int(h))
      await ctx.send("a area do quadrado de base {} e altura {} é: {}m²".format(b, h, area))
    else:
      await ctx.send("Os valores de base e altura devem ser positivos!")
  
  @commands.command(aliases=["areat"])
  async def _areat(self, ctx, b, h):
    if(int(b)>0 and int(h)> 0):
      area = (((int(b))*(int(h)))/2)
      await ctx.send("a area do triangulo de base {} e altura {} é: {}m²".format(b, h, area))
    else:
      print("os valores da base e da altura devem ser positivos")

  @commands.command()
  async def ping(self, ctx):
      await ctx.send("Pong! {}ms.".format(round(client.latency*1000)))
      
def setup(client):
  client.add_cog(matematica(client))