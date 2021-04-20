import discord


def help_cool_game():
    return [
        'Upon initiating the game you would be asked to set some characteristics.',
        'After Setting of characteristics, you would asked to enter a Number(Four-Digit).',
        'The entered number would be processed as a guess.',
        'After Processing \'Correct Digits\' and \'Correct Places\' would displayed which represent the correct digits and correct Places of the digits wrt to the random system generated number.',
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


# async def guild_join_message(guild):
#     found = False
#     welcome_channel = data_service.find_welcome_channel(guild.id)
#
#     if not welcome_channel:
#         return
#
#     await welcome_channel.send('Hello New Join is me')
