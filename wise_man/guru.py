import discord
import os
import requests
import json

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

WELCOME_CHANNEL_ID = -1
TRACKER_CHANNEL_ID = -1

#return motivation quotes randomly
def return_motivation():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_member_join(member):
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    await channel.send("{0}, welcome to the server, make sure you have fun.".format(member.name) + "\n" + return_motivation())

@client.event
async def on_member_remove(member):
    channel = member.guild.get_channel(TRACKER_CHANNEL_ID)
    await channel.send("hope {0} had fun.".format(member.name))


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

