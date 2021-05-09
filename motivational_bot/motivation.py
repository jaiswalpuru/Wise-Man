import discord
import os
import requests
import json

client = discord.Client()

def return_motivation():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    message.content = message.content.replace(" ", "")
    if message.content.startswith('$inspire'):
        await message.channel.send(return_motivation())

client.run(os.getenv("TOKEN"))

