import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class RoastBotClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}.'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = RoastBotClient()
client.run(TOKEN)