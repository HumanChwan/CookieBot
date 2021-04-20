import discord

import MathCookie
from data.cool_game import CoolGame
from data.guild import Guild
from data.member import Member


def create_cool_game() -> CoolGame:
    cool_game_temp = CoolGame()
    return cool_game_temp


def create_member(member_in_guild: discord.member) -> Member:
    member_to_store = Member()

    member_to_store.m_id = member_in_guild.id
    member_to_store.cool_game_data = create_cool_game()

    return member_to_store


def create_guild(guild: discord.guild):
    guild_to_stored = Guild()

    guild_to_stored._id = guild.id

    for channel_in_guild in guild.text_channels:
        guild_to_stored.welcome_channel_id = channel_in_guild.id
        break

    for member_in_guild in guild.members:
        guild_to_stored.member_list.append(create_member(member_in_guild))

    guild_to_stored.save()


def find_guild_by_id(guild_id: int) -> Guild:
    return Guild.objects(_id=guild_id).first()


def find_welcome_channel_id(id_to_be_searched: int) -> int:
    return find_guild_by_id(id_to_be_searched).welcome_channel_id


def add_member_to_guild(member: discord.member):
    guild = find_guild_by_id(member.guild.id)
    guild.member_list.append(create_member(member))

    guild.save()


def cool_game_turn_on(guild_id: int, member_id: int) -> bool:
    guild = find_guild_by_id(guild_id)

    for member in guild.member_list:
        if member.m_id == member_id:
            if member.cool_game_data.player_in_cool:
                return False
            member.cool_game_data.player_in_cool = True
            member.cool_game_data.tries = 10
            member.cool_game_data.temp_random = MathCookie.random_list()
            break

    guild.save()
    return True
    # -----> Member Edit <------- #


def cool_game_turn_off(guild_id: int, member_id: int) -> bool:
    guild = find_guild_by_id(guild_id)

    for member in guild.member_list:
        if member.m_id == member_id:
            if not member.cool_game_data.player_in_cool:
                return False
            member.cool_game_data.total_played += 1
            member.cool_game_data.player_in_cool = False
            break

    guild.save()
    return True
    # -----> Member Edit <------- #


def get_random(guild_id: int, member_id: int):
    guild = find_guild_by_id(guild_id)

    for member in guild.member_list:
        if member.m_id == member_id:
            return [member.cool_game_data.temp_random, member.cool_game_data.tries]


def update_member_cool_game_list(guild_id: int, member_id: int, completed: bool):
    guild = find_guild_by_id(guild_id)

    for member in guild.member_list:
        if member.m_id == member_id:
            member.cool_game_data.tries -= 1
            if completed or member.cool_game_data.tries == 0:
                member.cool_game_data.total_played += 1
                member.cool_game_data.player_in_cool = False
                if completed:
                    member.cool_game_data.total_won += 1
            break

    guild.save()


def player_playing(guild_id: int, member_id: int) -> bool:
    guild = find_guild_by_id(guild_id)

    for member in guild.member_list:
        if member.m_id == member_id:
            return member.cool_game_data.player_in_cool
