import os

import discord
from dotenv import load_dotenv
import Message
import Send
import dataService.data_service as dt_srv
import data.mongo_setup as mongo_setup

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.all()
client = discord.Client(intents=intents)


def mongo_launch():
    mongo_setup.mongo_init_()


@client.event
async def on_connect():
    print(f'{client.user.name} is ready to launch!')


@client.event
async def on_ready():
    # await client.change_presence(status=discord.Status.invisible)
    print(f'{client.user.name} launched!')


@client.event
async def on_member_join(member):
    if member.bot:
        return
    await member.create_dm()
    await member.dm_channel.send('yo hello')
    dt_srv.add_member_to_guild(member)


@client.event
async def on_guild_join(guild):
    dt_srv.create_guild(guild)
    await Send.guild_join_message(guild)
    dt_srv.emote_setup(guild.emojis)


@client.event
async def on_guild_emojis_update(guild: discord.guild, before, after):
    for emote in after:
        dt_srv.update_emote_exist(emote.name, emote.id, guild.id, emote.animated)


@client.event
async def on_message(message_meta):
    if message_meta.author.bot:
        return

    await Message.message_event_handling(message_meta)


mongo_launch()

client.run(TOKEN)
