import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class RoastBotClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}.'.format(self.user))

client = RoastBotClient()
client.run(TOKEN)