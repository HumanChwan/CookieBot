import os

import discord
from dotenv import load_dotenv
import MathCookie
import CoolGameFunc as CGF
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
    await member.create_dm()
    await member.dm_channel.send('yo hello')


@client.event
async def on_guild_join(guild):
    # await Send.guild_join_message(guild)
    dt_srv.create_guild(guild)

PlayersRn = {}

HelpCmd = ['help', 'cmd', 'command', 'commands']
QuitCmd = ['endgame', 'terminate', 'quit', 'exit', 'end']
prefix_acceptable = ['cookie', 'ck']

rimuru_spam_on = False


@client.event
async def on_message(message_meta):
    global PlayersRn
    global rimuru_spam_on

    if message_meta.author.bot:
        return

    prefix_in_use = prefix_acceptable

    # found = False
    # # SPAM MOMENT OREKI
    #
    # if message_meta.content == 'spam begin':
    #     rimuru_spam_on = True
    #     member_to_spammed = message_meta.author
    #
    #     for guild in client.guilds:
    #         for member in guild.members:
    #
    #             if not found and member.id == 689508374693281935:
    #                 member_to_spammed = member
    #                 found = True
    #                 break
    #         if found:
    #             break
    #
    #     await member_to_spammed.create_dm()
    #     while rimuru_spam_on:
    #         await member_to_spammed.dm_channel.send(
    #             'lol get spammed\n'
    #             + 'lol get spammed\n'
    #             + 'lol get spammed\n'
    #             + 'lol get spammed\n'
    #         )
    #     return
    #
    # if message_meta.content == 'stop spam':
    #     rimuru_spam_on = False
    #
    # return
    
    if MathCookie.check_integer(message_meta.content, False):
        if message_meta.author in PlayersRn:

            if len(message_meta.content) != 4:
                await message_meta.channel.send(f':cookie: **{message_meta.author.name} |** Wrong Input Style')

            elif CGF.repeat_found(message_meta.content):
                await message_meta.channel.send(f'<@{message_meta.author.id}> Found Repeated Digits in '
                                                f'the entered number :expressionless:')

            else:
                PlayersRn[message_meta.author][1] = message_meta.content

                partial_answer = CGF.check_log(PlayersRn[message_meta.author][0], PlayersRn[message_meta.author][1])

                embed_boi = discord.Embed(title='Guess Results',
                                          description='Player : ' + f'<@{message_meta.author.id}>')
                PlayersRn[message_meta.author][2] -= 1

                embed_boi.add_field(name='Correct Digits :', value=partial_answer[0])
                embed_boi.add_field(name='Correct Places :', value=partial_answer[1])
                embed_boi.add_field(name='Tries Left :', value=PlayersRn[message_meta.author][2])

                if partial_answer[1] == 4:
                    embed_boi.add_field(name='Guessed the Correct Number Yay :tada: :confetti_ball:', value='_ _')
                    PlayersRn.pop(message_meta.author)

                await message_meta.channel.send(content=None, embed=embed_boi)

                if message_meta.author in PlayersRn and PlayersRn[message_meta.author][2] == 0:

                    embed_two = discord.Embed(title='Ran Out of tries :disappointed:',
                                              description=f'<@{message_meta.author.id}> Better luck next Time UwU')
                    embed_two.add_field(name='Random Number was :', value=''.join(PlayersRn[message_meta.author][0]))

                    PlayersRn.pop(message_meta.author)

                    await message_meta.channel.send(content=None, embed=embed_two)

    message_as_list = message_meta.content.replace('`', '').replace('_', '').replace('|', '').split()

    if not message_as_list:
        return

    if message_as_list[0] in prefix_in_use:
        message_as_list.remove(message_as_list[0])

        if not message_as_list:
            await Send.cookie_quote(message_meta.channel)
            return

        if message_as_list[0].lower() in HelpCmd:
            await Send.embed_help(message_meta.channel)

        elif message_as_list[0] == 'math':
            message_as_list.remove('math')

            final_print = MathCookie.math_cookie(message_as_list)

            await message_meta.channel.send(f'\n :cookie: **{message_meta.author.name} |** ' + final_print)

        elif message_as_list[0].lower() == 'coolgame':
            message_as_list.remove(message_as_list[0])

            if not message_as_list or message_as_list[0].lower() in HelpCmd:
                await Send.embed_help_cool_game(message_meta.channel)

            elif message_as_list[0] == 'init':
                if message_meta.author in PlayersRn:
                    await message_meta.channel.send('Already initiated!! UwU')
                    return

                PlayersRn.update({message_meta.author: [MathCookie.random_list(), None, 10]})

                await message_meta.channel.send(f'<@{message_meta.author.id}>' + ' Game has now initiated ')

            elif message_as_list[0].lower() in QuitCmd:
                if message_meta.author in PlayersRn:
                    await Send.game_terminate(message_meta)

                    PlayersRn.pop(message_meta.author)
                else:
                    await message_meta.channel.send(f'<@{message_meta.author.id}> LOL what do you even wanna terminate,'
                                                    f' baka ka? :nerd:')
            else:
                await Send.embed_help_cool_game(message_meta.channel)

        elif message_as_list[0].lower() in {'simp', 'simprate', 'gay', 'gayrate'}:
            boi = MathCookie.random_between(0, 100)
            mention = message_meta.mentions
            to_be_mentioned = f'<@{message_meta.author.id}>'

            if mention:
                to_be_mentioned = f'<@{mention[0].id}>'

            if not mention:
                mention = message_meta.role_mentions
                if mention:
                    to_be_mentioned = f'{mention[0].mention}'

            end = 'gay'

            if message_as_list[0].lower() in {'simp', 'simprate'}:
                end = 'simp'

            await message_meta.channel.send(f'{to_be_mentioned} is {boi}% {end}')

        else:
            await Send.cookie_quote(message_meta.channel)

    elif message_as_list[0].lower() in QuitCmd:

        if message_meta.author in PlayersRn:
            await Send.game_terminate(message_meta)

            PlayersRn.pop(message_meta.author)
            return


mongo_launch()

client.run(TOKEN)
