import discord
import os
import requests as req
import json
import re
import string

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def get_roast(name):
    res = req.get(os.getenv('API_URL') + name)
    json_data = json.loads(res.text)
    return json_data['insult']


@client.event
async def on_ready():
    print('Logged on as: {0}.'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('!roast'):
        # Spaghetti code in order to not get errors when I pass a discord UID to an API request.
        pattern = r'[' + string.punctuation + ']'
        uid = message.author.mention
        stripped_uid = re.sub(pattern, '', uid)
        roast = get_roast(stripped_uid)
        roast = roast.replace(stripped_uid, uid)

        await message.channel.send(roast)

client.run(TOKEN)