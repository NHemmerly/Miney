# First Discord Bot maybe it'll get the weather or something

import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client = CustomClient(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    message_replies = [
        'Soji...',
        'giga',
        'return to the mines...'
    ]

    if message.content == 'hello bot':
        response = random.choice(message_replies)
        await message.channel.send(response)

@client.event
async def on_member_join(member):
    welcomeMessage = f'{member.name}, Welcome to the Basket!'
    channel = client.get_channel(1128026923679883327)
    await channel.send(welcomeMessage)

client.run(TOKEN)