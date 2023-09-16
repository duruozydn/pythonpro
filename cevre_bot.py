import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot=commands.Bot(command_prefix= '§', intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba Çevre Dostu {bot.user}! Ben bir botum!')

@bot.command()
async def soru(ctx):
    await ctx.send(f'Enerji tasarruflu {bot.user} ampuller kullanın')

bot.run('')
