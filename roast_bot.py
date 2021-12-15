import discord
import os
import requests as req
import json

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def get_roast():
    res = req.get('https://insult.mattbas.org/api/en/insult.json?who=Calin')
    json_data = json.loads(res.text)
    return json_data['insult']


@client.event
async def on_ready():
    print('Logged on as: {0}.'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content == '!roast':
        roast = get_roast()
        await message.channel.send(roast)

        #await message.channel.send('This is a roast.')

client.run(TOKEN)