import CoolGameHelp
import discord

async def EmbedHelp(Channel):
    embed_boi = discord.Embed(title="Command/Help", description="Shows the Commands and General overthrough of the Bot")
    embed_boi.add_field(name='ck CoolGame', value='ck CoolGame help\n ck CoolGame init\n ck CoolGame Terminate')
    embed_boi.add_field(name='ck math <expression>', value='\nCan Solve Math expressions : presently +, -, *, /, ^ are supported.')

    await Channel.send(content=None, embed=embed_boi)

async def EmbedHelpCG(Channel):
    embed_boi = discord.Embed(title='CoolGame Cmds and Help', description='CoolGame Commands')

    HelpCool = CoolGameHelp.helpCoolGame()

    i = 1
    for Instruction in HelpCool:
        embed_boi.add_field(name=str(i) + '. :cookie:', value=Instruction, inline=False)
        i += 1

    embed_boi.add_field(name='_ _', value='_ _', inline=False)
    embed_boi.add_field(name='HAVE FUN!', value='_ _', inline=False)

    await Channel.send(content=None, embed=embed_boi)

async def CookieQuote(channel):
    await channel.send('**Dood cookie? cookie what?** Now take this, idc')
    await channel.send(':cookie:')

async def GameTerminate(messageMETA):
    await messageMETA.channel.send(f':cookie: **{messageMETA.author.name} |** Game terminted :frowning:')