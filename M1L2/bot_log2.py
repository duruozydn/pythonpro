import random 

def gen_pass(pass_lenght):
    elements= 'awhdıauhdıughwldıushduaahduwşodıbskcvk'
    password= ''


for i in range(pass_length):
    password+= random.choice(elements)

return password


# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("MTE0NTAzMzY1OTY4MjkzNDkwNg.GJzSJ4.7Xn7s0CjFxK_jQr_TGAkxyjbdfe2q0JUmbtySQ")
