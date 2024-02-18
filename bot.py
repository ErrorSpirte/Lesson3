from bot_logic import *
import discord
import asyncio

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Здорова!")
    elif message.content.startswith('$bye'):
        await message.channel.send("Ладно, пока")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('Время замутить перекусончик 😎'):
        await asyncio.sleep(3)
        await message.channel.send('у меня тут в нычке 🧺')
        await asyncio.sleep(1.3)
        await message.channel.send('Вареные яички 🥚')
        await asyncio.sleep(1.85)
        await message.channel.send('Хлебушек 🍞')
        await asyncio.sleep(0.75)
        await message.channel.send('Консервы 🥫')
        await asyncio.sleep(0.8)
        await message.channel.send('и конечно кура-гриль 🍗')
        await asyncio.sleep(1.6)
        await message.channel.send('Маслята и лисички 🍄')
        await asyncio.sleep(1.75)
        await message.channel.send('Килограмм клубнички 🍓')
        await asyncio.sleep(1.65)
        await message.channel.send('Сосиски колбаса 🥩')
        await asyncio.sleep(1.4)
        await message.channel.send('и минералочки бутыль 💦')
    else:
        await message.channel.send(message.content)

client.run("Paste your token here")
