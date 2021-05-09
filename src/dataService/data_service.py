import discord

import MathCookie
from data.cool_game import CoolGame
from data.guild import Guild
from data.member import Member
from data.guild_show import GuildPretty
from data.member_show import MemberPretty
from functools import cmp_to_key
from data.emoji import Emoji


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
        if member_in_guild.bot:
            continue
        guild_to_stored.member_list.append(create_member(member_in_guild))

    guild_to_stored.save()


def find_guild_by_id(guild_id: int) -> Guild:
    return Guild.objects(_id=guild_id).first()


def update_emote_exist(name: str, e_id: int, g_id: int, animated: bool):
    emote = Emoji.objects(_id=e_id).first()

    if not emote:
        emote = Emoji()

        emote.name = name
        emote._id = e_id
        emote.guild_id = g_id
        emote.animated = animated

        emote.save()
        return

    if emote.name != name:
        emote.name = name
        emote.save()


def remove_emoji(e_id: int, e_name: str):
    emote = Emoji.objects(_id=e_id).first()
    if emote.name == e_name:
        emote.delete()


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


def compare(mem1: Member, mem2: Member):
    if mem1.cool_game_data.total_won > mem2.cool_game_data.total_won:
        return 1
    elif mem1.cool_game_data.total_won < mem2.cool_game_data.total_won:
        return -1
    else:
        if mem1.cool_game_data.total_played < mem2.cool_game_data.total_played:
            return 1
        elif mem1.cool_game_data.total_played > mem2.cool_game_data.total_played:
            return -1
        else:
            return 0


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

    guild.member_list = sorted(guild.member_list, key=cmp_to_key(compare), reverse=True)
    guild.save()


def player_playing(guild_id: int, member_id: int) -> bool:
    guild = find_guild_by_id(guild_id)

    for member in guild.member_list:
        if member.m_id == member_id:
            return member.cool_game_data.player_in_cool


def find_prefix_by_guild_id(guild_id: int):
    guild = find_guild_by_id(guild_id)

    return guild.prefix_acceptable


def get_guild_data(guild_id: int) -> GuildPretty:
    guild = find_guild_by_id(guild_id)
    guild_return = GuildPretty()
    guild_return._id = guild_id

    list_data = [[x.cool_game_data.total_won, x.m_id] for x in guild.member_list]

    # list_data.sort(key=lambda x: x[0], reverse=True)

    len_list_data = len(list_data)

    if len_list_data > 0:
        guild_return.cool_game_data['One'] = list_data[0]
        len_list_data -= 1

    if len_list_data > 0:
        guild_return.cool_game_data['Two'] = list_data[1]
        len_list_data -= 1

    if len_list_data > 0:
        guild_return.cool_game_data['Three'] = list_data[2]

    return guild_return


def get_member_data(m_id: int, guild_id: int) -> MemberPretty:
    guild = find_guild_by_id(guild_id)
    member_return = MemberPretty()
    i = 1
    member = None
    for member in guild.member_list:
        if member.m_id == m_id:
            break
        i += 1
    if member:
        member_return.total_won = member.cool_game_data.total_won
        member_return.total_played = member.cool_game_data.total_played
        member_return.rank = i

    return member_return


def emote_setup(emojis):
    for d_emote in emojis:
        emote = Emoji()

        emote.name = d_emote.name
        emote._id = d_emote.id
        emote.guild_id = d_emote.guild.id
        emote.animated = d_emote.animated

        emote.save()


def get_emote(g_id: int):
    return Emoji.objects()
    # emote_list = Emoji.objects(name=name)
    #
    # if not emote_list:
    #     pass
    # emote = emote_list[0]
    # for emote in emote_list:
    #     if emote.guild_id == g_id:
    #         return emote
    #
    # return emote


def cnt_emote():
    return Emoji.objects.count()


def get_emotes(start: int, end: int):
    if start == 0:
        return Emoji.objects[:end]
    emotes = Emoji.objects[start:end]
    if emotes is None:
        emotes = Emoji.objects[start:]
    return emotes
