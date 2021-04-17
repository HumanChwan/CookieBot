import os

import discord
from dotenv import load_dotenv
import random

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


def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0


def CheckInteger(num, If_Dot):
    cnt = 0
    for i in num:
        if i == '.':
            cnt += 1
            if cnt == If_Dot+1:
                return False 
        elif i < '0' or '9' < i:
            return False

    return True


def Best(numStr):
    if numStr[0] == '.':
        numStr = '0' + numStr
    elif numStr[-1] == '.':
        numStr += '0'

    return numStr

def InfixtoPostix(inf):
    stack = []
    PostfixList = []
    for j in inf:
        if CheckInteger(j, True):
            PostfixList.append(Best(j))
        elif j == '(':
            stack.append('(')
        elif j == ')':
            while stack[-1] != '(' and stack:
                PostfixList.append(stack[-1])
                stack.pop()
            stack.pop()
        elif j == '^':
            stack.append('^')
        else:
            if stack and precedence(j) >= precedence(stack[-1]):
                stack.append(j)
            else:
                while stack and precedence(j) < precedence(stack[-1]):
                    PostfixList.append(stack[-1])
                    stack.pop()
                stack.append(j)
        
    while stack:
        PostfixList.append(stack[-1])
        stack.pop()
    return PostfixList


def addition(a, b):
    return a+b

def subtraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def division(a, b):
    return a/b

def exponent(a, b):
    return a**b


def Arth(func, a, b):
    return func(a, b)

function_name = {
    '+' : addition,
    '-' : subtraction,
    '*' : multiplication,
    '/' : division,
    '^' : exponent
}

def evaluate(PostfixList):
    stack = []
    for j in PostfixList:
        if CheckInteger(j, True):
            stack.append(j)
        else:
            one = float(stack[-1])
            stack.pop()
            two = float(stack[-1])
            stack.pop()
            stack.append(str(Arth(function_name[j], two, one)))
    answer = float(stack[-1])
    return answer


def stringToInfixList(inf):
    cache = ''
    FinalInfixList = []
    for c in inf:
        if c == ' ' and cache != '':
            FinalInfixList.append(cache)
            cache = ''
        elif '0' <= c <= '9' or c == '.':
            cache += c
        elif c in {'+', '-', '*', '/', '^', '(', ')'}:
            if cache != '':
                FinalInfixList.append(cache)
                cache = ''
            FinalInfixList.append(c)
    if cache != '':
        FinalInfixList.append(cache)
        cache = ''
    return FinalInfixList


def ExpressionProcessor(InfixString):
    InfixList = stringToInfixList(InfixString)
    PostfixList = InfixtoPostix(InfixList)

    return evaluate(PostfixList)

def MathCookie(InfixLst):
    if not InfixLst:
        return 'Incorrect expression? At least get your shit right man :pensive:'

    Answer = ExpressionProcessor(' '.join(InfixLst))

    if Answer == None:
        return 'Incorrect expression? At least get your shit right man :pensive:'

    return 'Nice there you go, Your expression yieldeth : ' + '**' + f'{Answer}' + '**'
    

# def helpTXT():
#     return (
#         + f'prefix to summon the Bot - {prefix}\n'
#         + '1. Use *cookie math <expression>* for solving math equations : presently +, -, *, /, ^ are supported.\n'
#         + '2. Use *cookie CoolGame init* to initiate the game.\n'
#         + '3. For now thats pretty much it. :smile:\n'
#     )

def helpCoolGame():
    return [
        'Upon initiating the game you would be asked to set some characterstics.',
        'After Setting of characterstics, you would asked to enter a Number(Four-Digit).',
        'The entered number would be processed as a guess.',
        'After Processing \'Correct Digits\' and \'Correct Places\' would displayed which represent the correct digits and correct Places of the digits wrt to the random system generated number.',
        'Following the end of maximum guesses or by guessing the Correct the number, game will end. :thumbs_up:'
        'Time Out for entering the number is set at 5 minutes after which game will terminate automatically.',
        'Entering EndGame will terminate the game in between the game.',
    ]

def RandomList():
    first10 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while first10[0] == '0':
        random.shuffle(first10)
    return [first10[i] for i in range(4)]


PlayersRn = {}


def Checklog(a, b):
    cnt_dig = cnt_plc = 0
    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] == b[i]:
                cnt_dig += 1
                if i == j:
                    cnt_plc += 1
    return [cnt_dig, cnt_plc]

def RepeatFound(InputStr):
    boolDig = [False] * 10
    for i in InputStr:
        if boolDig[int(i)-int('0')]:
            return True
        else:
            boolDig[int(i)-int('0')] = True
    return False

PrefixAcceptable = ['cookie', 'ck']

@client.event
async def on_message(messageMETA):
    global PlayersRn
 
    if messageMETA.author.bot:
        return

    PrefixInUse = PrefixAcceptable

    if CheckInteger(messageMETA.content, False):
        if messageMETA.author in PlayersRn:
            if len(messageMETA.content) != 4:
                await messageMETA.channel.send('Wrong Input Style')
            elif RepeatFound(messageMETA.content):
                await messageMETA.channel.send(f'<@{messageMETA.author.id}> Found Repeated Digits in the entered number :expressionless:')
            else:
                PlayersRn[messageMETA.author][1] = messageMETA.content

                PartAns = Checklog(PlayersRn[messageMETA.author][0], PlayersRn[messageMETA.author][1])

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
                    PlayersRn.pop(messageMETA.author)
                    await messageMETA.channel.send(content=None, embed=embed_two)
    
    MessageLst = messageMETA.content.split()
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

            FinalPrint = MathCookie(MessageLst)

            await messageMETA.channel.send(f'\n <@{messageMETA.author.id}> ' + FinalPrint)

        elif MessageLst[0].lower() == 'coolgame':
            MessageLst.remove(MessageLst[0])

            if not MessageLst or MessageLst[0] in {'help', 'cmd', 'command'}:
                embed_boi = discord.Embed(title='CoolGame Cmds and Help', description='CoolGame Commands')
                HelpCool = helpCoolGame()
                for i in range(len(HelpCool)):
                    embed_boi.add_field(name=str(i+int('1')) + '.', value=HelpCool[i])
                embed_boi.add_field(name='_ _', value='_ _')
                embed_boi.add_field(name='HAVE FUN!', value='_ _')
                await messageMETA.channel.send(content=None, embed=embed_boi)
            elif MessageLst[0] == 'init':
                if messageMETA.author in PlayersRn:
                    await messageMETA.channel.send('Already initiatd!! UwU')
                    return
                PlayersRn.update({messageMETA.author : [RandomList(),None, 1]})
                await messageMETA.channel.send(f'<@{messageMETA.author.id}>'  + ' Game has now initiated ')
                print(PlayersRn[messageMETA.author][0])
            elif MessageLst[0].lower() in {'endgame','terminate', 'quit','exit'}:
                if messageMETA.author in PlayersRn:
                    await messageMETA.channel.send(f'<@{messageMETA.author.id}> Game terminted :frowning:')
                    PlayersRn.pop(messageMETA.author)
                    return
                else:
                    await messageMETA.channel.send(f'<@{messageMETA.author.id}> LOL what do you even wanna terminate, baka ka? :nerd:')
                    return
            else:
                embed_boi = discord.Embed(title='CoolGame Cmds and Help', description=helpCoolGame())
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