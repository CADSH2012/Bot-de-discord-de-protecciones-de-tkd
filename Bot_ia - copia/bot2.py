
import discord, random

from discord.ext import commands
from clasificador import clasf

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, {bot.user}!')
        
@bot.group()
async def cool(ctx):
    
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} no es cool') 
    
@cool.command(name='Mi_primer_bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Si, el bot es cool.')

@cool.command(name='El_pais_etrisde')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Si, el pais etrisde es cool.')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name= attachment.filename
            image_extensions = ('.jpg','.jpeg', '.png')

            if file_name.endswith(image_extensions):
                await attachment.save(f"./images/{file_name}")
                await ctx.send(clasf(f"./images/{file_name}"))

            else:
                await ctx.send("La imagen no es una archivo valido.")
    else:
        await ctx.send("No se ha adjuntado ningun archivo")


bot.run("MTI5OTUyNDY1NjkwMjA0NTY5Ng.GtYjr5.ppdKTE3kjEtPv7TkRk7BMjI1LVMXSI70VsbXt7A")