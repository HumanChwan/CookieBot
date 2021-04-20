# import os
# import discord
# from dotenv import load_dotenv
# from pymongo import MongoClient
#
# from data.guild import Guild
# from data.member import Member
#
# load_dotenv()


# def create_member(member: discord.Member):
#     member_temp = Member()
#     member_temp.member_Id = member.id
#     member_temp.CoolGameData = {
#         'CoolGameINIT': False,
#         'TotalPlayed': 0,
#         'TotalWon': 0
#     }
#
#     member_db.insert_one({
#         '_id': member_temp.member_Id,
#         'cool_game_data': {
#             'CoolGameINIT': False,
#             'TotalPlayed': 0,
#             'TotalWon': 0
#         }
#     })


# def create_guild(guild: discord.guild):
#     guild_temp = Guild()
#
#     for channel in guild.channels:
#         guild_temp.welcome_channel = channel
#         break
#
#     guild_temp.PrefixAcceptable = ['cookie', 'ck']
#     guild_temp.guild_id = guild.id
#
#     list_of_members = []
#     for member in guild.members:
#         create_member(member)
#         list_of_members.append(member)
#
#     guild_db.insert_one({
#         '_id': guild_temp.guild_id,
#         'prefix_acceptable': ['cookie', 'ck'],
#         'players': list_of_members
#     })

#
# def find_welcome_channel(guild_id_asked):
#
#     for guild_found in guild_db.find({}):
#         if guild_found.guild_id == guild_id_asked:
#             break
#
#     if not guild_found.welcome_channel:
#         return guild_found.welcome_channel
#     else:
#         return None


import discord

from data.cool_game import CoolGame
from data.guild import Guild
from data.member import Member


def create_cool_game() -> CoolGame:
    cool_game_temp = CoolGame()
    return cool_game_temp


def create_member(member_in_guild: discord.member) -> Member:
    member_to_store = Member()

    member_to_store.member_Id = str(member_in_guild.id)
    member_to_store.cool_game_data = create_cool_game()

    return member_to_store


def create_guild(guild: discord.guild):
    guild_to_stored = Guild()

    guild_to_stored.guild_id = str(guild.id)

    for channel_in_guild in guild.channels:
        guild_to_stored.welcome_channel_id = str(channel_in_guild.id)
        break

    for member_in_guild in guild.members:
        guild_to_stored.member_list.append(create_member(member_in_guild))

    guild_to_stored.save()
