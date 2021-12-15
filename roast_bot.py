import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('Logged on as: {0}.'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content == '!roast':
        await message.channel.send('Ur ugly lol')

client.run(TOKEN)