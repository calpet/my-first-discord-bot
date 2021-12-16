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

def handle_request(message):
    # Spaghetti code in order to not get errors when I pass a discord UID to an API request.
    pattern = r'[' + string.punctuation + ']'
    uid = message.content.split()[1]
    stripped_uid = re.sub(pattern, '', uid)
    result = get_roast(stripped_uid).replace(stripped_uid, uid)
    return result

@client.event
async def on_ready():
    print('Logged on as: {0}.'.format(client.user))

# This is the event handler where we add our custom commands.
@client.event
async def on_message(message):
    # Prevent infinite bot loops.
    if message.author == client.user:
        return
        
    if message.content.startswith('!roast'):
        roast = handle_request(message)
        await message.channel.send(roast)

client.run(TOKEN)