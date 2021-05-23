import discord
import os
import logging
import random

from dotenv.main import dotenv_values

from internal.helper import check_language
from adapters.quotes import return_motivation
from internal.enums import Enums, Internal_Error, Games

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents,command_prefix='$')

config = dotenv_values(".env")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    random_game = random.choice(Games)
    await client.change_presence(activity = discord.Game(random_game))

@client.event
async def on_member_join(member):
    channel = member.guild.get_channel(config.get(Enums.wc_id.value))
    await channel.send("{0}, welcome to the server, make sure you have fun.".format(member.name) + "\n" + return_motivation())

@client.event
async def on_member_remove(member):
    channel = member.guild.get_channel(config.get(Enums.tc_id.value))
    await channel.send("hope {0} had fun.".format(member.name))

@client.event
async def on_message(message):
    
    #to avoid recursion
    if message.author == client.user:
        return
    
    #message function map
    switch = {
        message.content.startswith('$inspire') : return_motivation,
        message.content.startswith('$com') : check_language,
    }

    try:
        await message.channel.send(switch.get(message.content.startswith(message.content))(message.content))
    except:
        logging.warning(Internal_Error.NOT_DEFINED.value)


client.run(os.getenv(Enums.token.value,config.get(Enums.token.value)))

