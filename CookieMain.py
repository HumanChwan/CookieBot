import os

import discord
from dotenv import load_dotenv
import MathCookie
import CoolGameHelp
import CoolGameFunc as cgf

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_connect():
    print(f'{client.user.name} is ready to launch!')

@client.event
async def on_ready():
    print(f'{client.user.name} launched!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send('yo hello')

# @client.event
# async def on_guild_join(guild):

PlayersRn = {}

PrefixAcceptable = ['cookie', 'ck']

@client.event
async def on_message(messageMETA):
    global PlayersRn
 
    if messageMETA.author.bot:
        return

    PrefixInUse = PrefixAcceptable

    if MathCookie.CheckInteger(messageMETA.content, False):
        if messageMETA.author in PlayersRn:
            
            if len(messageMETA.content) != 4:
                await messageMETA.channel.send('Wrong Input Style')

            elif cgf.RepeatFound(messageMETA.content):
                await messageMETA.channel.send(f'<@{messageMETA.author.id}> Found Repeated Digits in the entered number :expressionless:')

            else:
                PlayersRn[messageMETA.author][1] = messageMETA.content

                PartAns = cgf.Checklog(PlayersRn[messageMETA.author][0], PlayersRn[messageMETA.author][1])

                embed_boi = discord.Embed(title='Guess Results', description='Player : ' + f'<@{messageMETA.author.id}>')
                PlayersRn[messageMETA.author][2] -= 1

                embed_boi.add_field(name='Correct Digits :', value=PartAns[0])
                embed_boi.add_field(name='Correct Places :', value=PartAns[1])
                embed_boi.add_field(name='Tries Left :', value=PlayersRn[messageMETA.author][2])

                if PartAns[1] == 4:
                    embed_boi.add_field(name='Guessed the Correct Number Yay :tada: :confetti_ball:', value='_ _')
                    PlayersRn.pop(messageMETA.author)

                await messageMETA.channel.send(content=None, embed=embed_boi)

                if messageMETA.author in PlayersRn and PlayersRn[messageMETA.author][2] == 0:

                    embed_two = discord.Embed(title='Ran Out of tries :disappointed:', description=f'<@{messageMETA.author.id}> Better luck next Time UwU')
                    embed_two.add_field(name='Random Number was :', value=''.join(PlayersRn[messageMETA.author][0]))

                    PlayersRn.pop(messageMETA.author)
                    
                    await messageMETA.channel.send(content=None, embed=embed_two)

    MessageLst = messageMETA.content.replace('`', '').replace('_', '').split()

    if not MessageLst:
        return

    if MessageLst[0] in PrefixInUse:
        MessageLst.remove(MessageLst[0])

        if not MessageLst:
            await messageMETA.channel.send('**Dood cookie? cookie what?** Now take this, idc')
            await messageMETA.channel.send(':cookie:')
            return

        if MessageLst[0].lower() in {'help', 'cmd', 'command'}: 

            embed_boi = discord.Embed(title="Command/Help", description="Shows the Commands and General overthrough of the Bot")
            embed_boi.add_field(name='ck CoolGame', value='ck CoolGame help\n ck CoolGame init\n ck CoolGame Terminate')
            embed_boi.add_field(name='ck math <expression>', value='\nCan Solve Math expressions : presently +, -, *, /, ^ are supported.')

            await messageMETA.channel.send(content=None, embed=embed_boi)

        elif MessageLst[0] == 'math':
            MessageLst.remove('math')

            FinalPrint = MathCookie.MathCookie(MessageLst)

            await messageMETA.channel.send(f'\n <@{messageMETA.author.id}> ' + FinalPrint)

        elif MessageLst[0].lower() == 'coolgame':
            MessageLst.remove(MessageLst[0])

            if not MessageLst or MessageLst[0].lower() in {'help', 'cmd', 'command'}:

                embed_boi = discord.Embed(title='CoolGame Cmds and Help', description='CoolGame Commands')
                HelpCool = CoolGameHelp.helpCoolGame()

                for i in range(len(HelpCool)):
                    embed_boi.add_field(name=str(i+int('1')) + '.', value=HelpCool[i])

                embed_boi.add_field(name='_ _', value='_ _')
                embed_boi.add_field(name='HAVE FUN!', value='_ _')

                await messageMETA.channel.send(content=None, embed=embed_boi)

            elif MessageLst[0] == 'init':
                if messageMETA.author in PlayersRn:
                    await messageMETA.channel.send('Already initiatd!! UwU')
                    return

                PlayersRn.update({messageMETA.author : [cgf.RandomList(), None, 10]})

                await messageMETA.channel.send(f'<@{messageMETA.author.id}>'  + ' Game has now initiated ')

            elif MessageLst[0].lower() in {'endgame','terminate', 'quit','exit'}:
                if messageMETA.author in PlayersRn:
                    await messageMETA.channel.send(f'<@{messageMETA.author.id}> Game terminted :frowning:')
                    PlayersRn.pop(messageMETA.author)
                    return
                else:
                    await messageMETA.channel.send(f'<@{messageMETA.author.id}> LOL what do you even wanna terminate, baka ka? :nerd:')
                    return
            else:
                embed_boi = discord.Embed(title='CoolGame Cmds and Help', description='CoolGame Commands')

                HelpCool = CoolGameHelp.helpCoolGame()

                for i in range(len(HelpCool)):
                    embed_boi.add_field(name=str(i+int('1')) + '.', value=HelpCool[i])

                embed_boi.add_field(name='_ _', value='_ _')
                embed_boi.add_field(name='HAVE FUN!', value='_ _')

                await messageMETA.channel.send(content=None, embed=embed_boi)

        else:
            await messageMETA.channel.send('**Dood cookie? cookie what?** Now take this, idc')
            await messageMETA.channel.send(':cookie:')

            return
    elif MessageLst[0].lower() in {'endgame','terminate', 'quit','exit'}:

        if messageMETA.author in PlayersRn:
            await messageMETA.channel.send(f'<@{messageMETA.author.id}> Game terminted :frowning:')

            PlayersRn.pop(messageMETA.author)
            return

client.run(TOKEN)   