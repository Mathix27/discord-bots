import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.command()
async def prog_list(ctx):
    await ctx.send(os.listdir("clase 5/programacion"))
    
@bot.command()
async def juego_list(ctx):
    await ctx.send(os.listdir("clase 5/juegos"))
    
@bot.command()
async def animal_list(ctx):
    await ctx.send(os.listdir("clase 5/animales"))

#-------------------------------------------------------------------------------------------------------------------

@bot.command()
async def mem_progra(ctx):
    list_prog = os.listdir("clase 5/programacion")
    ruta = f"clase 5/programacion/{random.choice(list_prog)}"
    with open(ruta, "rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
    
@bot.command()
async def mem_juego(ctx):
    list_juego = os.listdir("clase 5/juegos")
    ruta = f"clase 5/juegos/{random.choice(list_juego)}"
    with open(ruta, "rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
        
@bot.command()
async def mem_animal(ctx):
    list_animal = os.listdir("clase 5/animales")
    ruta = f"clase 5/animales/{random.choice(list_animal)}"
    with open(ruta, "rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
  
#--------------------------------------------------------------------------------------------------------

@bot.command()
async def m1(ctx):
    with open("clase 5/Img/m1.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
    
@bot.command()
async def m2(ctx):
    with open("clase 5/Img/m2.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
    
@bot.command()
async def m3(ctx):
    with open("clase 5/Img/m3.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
    


bot.run("your token")