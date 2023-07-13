# First Discord Bot maybe it'll get the weather or something

import os
import subprocess

import discord
import random
from json import load
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client = CustomClient(intents=discord.Intents.all())

with open('keywords.json') as keyword_file:
    keywords = load(keyword_file)

async def send_command(keyword):
    keyword = str[1:]
    if keyword in keywords['standard_commands']:
        keyword = keywords['standard_commands'][keyword]
    try:
         resp = subprocess.Popen([keyword], shell=True, stdout=subprocess.PIPE)
         status = resp.poll()
    except:
        resp = 'Something went wrong'

@client.event
async def on_message(message):
    if not message.content.startswith('>') or message.author == client.user:
        return
    
    try:
         resp = subprocess.Popen([message], shell=True, stdout=subprocess.PIPE)
         status = resp.poll()
    except:
        resp = 'Something went wrong'
    #message_replies = [
     #   'Soji...',
     #   'giga',
      #  'return to the mines...'
    #]

    #if message.content == 'hello bot':
     #   response = random.choice(message_replies)
      #  await message.channel.send(response)

@client.event
async def on_member_join(member):
    welcomeMessage = f'{member.name}, Welcome to the Basket!'
    channel = client.get_channel(1128026923679883327)
    await channel.send(welcomeMessage)

client.run(TOKEN)