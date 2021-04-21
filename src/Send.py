import discord
import dataService.data_service as dt_srv
from data.guild_show import GuildPretty


def help_cool_game():
    return [
        'Upon initiating the game you would be asked to set some characteristics.',
        'After Setting of characteristics, you would asked to enter a Number(Four-Digit).',
        'The entered number would be processed as a guess.',
        'After Processing \'Correct Digits\' and \'Correct Places\' would displayed '
        + 'which represent the correct digits and correct Places of the digits '
        + 'wrt to the random system generated number.',
        'Following the end of maximum guesses or by guessing the Correct the number, game will end. :thumbsup:'
        'Time Out for entering the number is set at 5 minutes after which game will terminate automatically.',
        'Entering EndGame will terminate the game in between the game.',
    ]


async def embed_help(channel):
    embed_boi = discord.Embed(title="Command/Help",
                              description="Shows the Commands and General over-through of the Bot")
    embed_boi.add_field(name='ck CoolGame', value='ck CoolGame help\n ck CoolGame init\n ck CoolGame Terminate')
    embed_boi.add_field(name='ck math <expression>',
                        value='\nCan Solve Math expressions : presently +, -, *, /, ^ are supported.')

    await channel.send(content=None, embed=embed_boi)


async def embed_help_cool_game(channel):
    embed_boi = discord.Embed(title='CoolGame Cmds and Help', description='CoolGame Commands')

    help_cool = help_cool_game()

    i = 1
    for Instruction in help_cool:
        embed_boi.add_field(name=str(i) + '. :cookie:', value=Instruction, inline=False)
        i += 1

    embed_boi.add_field(name='_ _', value='_ _', inline=False)
    embed_boi.add_field(name='HAVE FUN!', value='_ _', inline=False)

    await channel.send(content=None, embed=embed_boi)


async def cookie_quote(channel):
    await channel.send('**Dood cookie? cookie what?** Now take this, idc')
    await channel.send(':cookie:')


async def game_terminate(message_meta):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |** Game terminated :frowning:')


async def guild_join_message(guild):
    channel_id = dt_srv.find_welcome_channel_id(guild.id)

    if not channel_id:
        return

    channel = guild.get_channel(channel_id)
    await channel.send('Hi! Yo doods')


async def wrong_input(message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |**' +
                                    ' Wrong Input Style :frowning:')


async def incorrect_expression(message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |**' +
                                    ' Incorrect expression? At least get your shit right man :pensive:')


async def correct_expression(answer: int, message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |** Nice there you go,' +
                               f' Your expression yieldeth : **{answer}**')


async def parallel_init_error(message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |**' +
                                    ' Already initiated! UwU :smile:')


async def init_successful(message_meta: discord.message):
    embed_one = discord.Embed(title='Game has Initialised', description=f'Player: <@{message_meta.author.id}>')
    embed_one.add_field(name='Tries : ', value='10', inline=False)
    embed_one.set_image(url='https://static.toiimg.com/photo/72975551.cms')

    await message_meta.channel.send(content=None, embed=embed_one)


async def empty_terminate_error(message_meta: discord.message):
    await message_meta.channel(f':cookie: **{message_meta.author.name} |**' +
                               ' Lol! what do you wanna terminate? _B A K A_ :nerd:')


async def terminate_successful(message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |**' +
                                    ' Game terminated _sad moment_ :disappointed:')


async def repeat_input(message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |**' +
                                    ' Found Repeated Digits _sad moment_ :expressionless:')


async def publish_result(message_meta: discord.message, partial_result, tries_left: int):
    embed_one = discord.Embed(title='Guess Results', description=f'Player: <@{message_meta.author.id}>')
    embed_one.add_field(name='Correct Digits:', value=str(partial_result[0]))
    embed_one.add_field(name='Correct Places:', value=str(partial_result[1]))
    embed_one.add_field(name='Tries Left:', value=str(tries_left))
    if partial_result[1] == 4:
        embed_one.add_field(name='Guessed the Correct Number :tada: :confetti_ball:', value='_ _')

    await message_meta.channel.send(content=None, embed=embed_one)


async def ran_out_of_tries(message_meta: discord.message, param):
    embed_one = discord.Embed(title='Ran Out Of Tries :disappointed:',
                              description=f'Player: <@{message_meta.author.id}>')
    embed_one.add_field(name='Better Luck Next Time :thumbsup:', value='_ _', inline=False)
    embed_one.add_field(name='The Random number was :', value=param[0]+param[1]+param[2]+param[3])

    await message_meta.channel.send(content=None, embed=embed_one)


async def present_guild_data(guild_data: GuildPretty, guild_discord: discord.guild, channel: discord.channel):
    embed_boi = discord.Embed(title='Cookie Stats ', description='_ _')
    # embed ------> guild_discord.name
    if guild_data.cool_game_data['One'][1]:
        one = guild_data.cool_game_data['One']
        member = guild_discord.get_member(one[1])
        display_name = member.nick
        if not display_name:
            display_name = member.name
        leaderboard = f'**1.** __**{display_name}**__ : **{one[0]}**\n'
        # embed ----- > guild_discord.get_member(guild_data.cool_game_data['One'][1])
    else:
        leaderboard = f'**1.** ------- : ----\n'

    if guild_data.cool_game_data['Two'][1]:
        two = guild_data.cool_game_data['Two']
        member = guild_discord.get_member(two[1])
        display_name = member.nick
        if not display_name:
            display_name = member.name
        leaderboard += f'**2.** __**{display_name}**__ : **{two[0]}**\n'
        # embed ----- > guild_discord.get_member(guild_data.cool_game_data['One'][1])
    else:
        leaderboard += f'**2.** ------- : ----\n'
        # embed ---- > empty

    if guild_data.cool_game_data['Three'][1]:
        three = guild_data.cool_game_data['Three']
        member = guild_discord.get_member(three[1])
        display_name = member.nick
        if not display_name:
            display_name = member.name
        leaderboard += f'**3.** __**{display_name}**__ : **{three[0]}**\n'
        # embed ----- > guild_discord.get_member(guild_data.cool_game_data['One'][1])
    else:
        leaderboard += f'**3.** ------- : ----\n'
        # embed ---- > empty

    embed_boi.add_field(name=f'__Leaderboard of {guild_discord.name}__', value=leaderboard, inline=False)
    # embed ----> guild.discord.member_count
    embed_boi.add_field(name='Member Count:', value=str(guild_discord.member_count))

    embed_boi.set_footer(text=f'Server id: {guild_discord.id}')
    # mbed.footer -----> guild_discord.id
    await channel.send(content=None, embed=embed_boi)
