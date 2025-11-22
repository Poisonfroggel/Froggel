import discord
from discord.ext import commands
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme/FrogMemes')
  json_data = json.loads(response.text)
  return json_data['url']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send('Hello! Ribbit!')

    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run() # Replace with your own token.

