import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot=commands.Bot(command_prefix= '§', intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba Çevre Dostu {bot.user}! Ben bir botum!, Yönergeleri okumak için §yonerge yaz!')

@bot.command()
async def yonerge(ctx):
    await ctx.send(f'Yönergeler: §soru ve §cevre yazarak çevre kirliiğini önlemek amaçlı fikirler bulabilirsin. Günümüzde çevre kirliliği çok fazla bu sebeple eğer bunun çözümüne bir adım attıysan seni tebrik ediyoruz!')


@bot.command()
async def soru(ctx):
    await ctx.send(f'Enerji tasarruflu  ampuller kullanın')


@bot.command()
async def cevre(ctx):
    await ctx.send(f'Kağıt havlu kullanımını azaltın')


fazla_soru= int(input('Daha fazla çözüm için 1 yazın'))
fazla= int(input('Gelecekteki çevre kirliliği ile ilgili fotoğraf almak için 2 yazın'))

if fazla_soru== 1:
    @bot.command()
    async def fazla(ctx):
        await ctx.send(f'Naylon poşet kullanımınıı azaltın')

elif fazla== 2:
    @bot.command()
    async def foto(ctx):
        await ctx.send(f'M1L2/images/cevre-kirliligi.png')
        await ctx.send(f'M1L2/images/2760348_1200x627.png')




bot.run('')
