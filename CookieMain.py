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

stack = []

def push(entry): 
    stack.append(entry)

def pop():
    if not stack:
        print("Empty PStack")
        return
    stack.pop()

def peek():
    if not stack:
        print("Empty KStack")
        return
    return stack[-1]

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0


def CheckInteger(num, thresholddot):
    cnt = 0
    for i in num:
        if i == '.':
            cnt += 1
            if cnt == thresholddot+1:
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
    push('#')
    PostfixList = []
    for j in inf:
        if CheckInteger(j, 1):
            PostfixList.append(Best(j))
        elif j == '(':
            push('(')
        elif j == ')':
            while peek() != '(' and peek() != '#':
                PostfixList.append(peek())
                pop()
            pop()
        elif j == '^':
            push('^')
        else:
            if precedence(j) >= precedence(peek()):
                push(j)
            else:
                while peek() != '#' and precedence(j) < precedence(peek()):
                    PostfixList.append(peek())
                    pop()
                push(j)
        
    while peek() != '#':
        PostfixList.append(peek())
        pop()
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
    for j in PostfixList:
        if CheckInteger(j, 1):
            push(j)
        else:
            one = float(peek())
            pop()
            two = float(peek())
            pop()
            push(str(Arth(function_name[j], two, one)))
    answer = float(peek())
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
    
prefix = 'cookie'

def helpTXT():
    return (
        + f'prefix to summon the Bot - {prefix}\n'
        + '1. Use *cookie math <expression>* for solving math equations : presently +, -, *, /, ^ are supported.\n'
        + '2. Use *cookie CoolGame init* to initiate the game.\n'
        + '3. For now thats pretty much it. :smile:\n'
    )

def helpCoolGame():
    return (
        '1. Upon initiating the game you would be asked to set some characterstics.\n'
        + '2. After Setting of characterstics, you would asked to enter a Number(Four-Digit).\n'
        + '3. The entered number would be processed as a guess.\n'
        + '4. After Processing \'Correct Digits\' and \'Correct Places\' would displayed which represent the correct digits and correct Places of the digits wrt to the random system generated number.\n'
        + '5. Following the end of maximum guesses or by guessing the Correct the number, game will end. :thumbs_up:\n'
        + '6. Time Out for entering the number is set at 5 minutes after which game will terminate automatically.\n'
        + '7. Entering EndGame will terminate the game in between the game.\n'
        + '\n HAVE FUN!'
    )

def RandomList():
    first9 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(first9)
    return [first9[i] for i in range(4)]


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


@client.event
async def on_message(messageMETA):
    global PlayersRn

    if messageMETA.author.bot:
        return

    if CheckInteger(messageMETA.content, 0):
        if messageMETA.author in PlayersRn:
            if PlayersRn[messageMETA.author][0] != 0:
                if len(messageMETA.content) != 4:
                    await messageMETA.channel.send('Wrong Input Style')
                else:
                    PlayersRn[messageMETA.author][1] = messageMETA.content
                    PartAns = Checklog(PlayersRn[messageMETA.author][0], PlayersRn[messageMETA.author][1])
                    embed_boi = discord.Embed(title='Guess Results')
                    embed_boi.add_field(name='Correct Digits :', value=f'{PartAns[0]}')
                    embed_boi.add_field(name='Correct Places :', value=f'{PartAns[1]}')
                    if PartAns[1] == 4:
                        embed_boi.add_field(name='Guessed the Correct Number Yay :tada: :confetti_ball:', value=None)
                        PlayersRn.pop(messageMETA.author)
                    await messageMETA.channel.send(content=None, embed=embed_boi)

    
    MessageLst = messageMETA.content.split()
    if not MessageLst:
        return

    if MessageLst[0] == 'cookie':
        MessageLst.remove('cookie')

        if not MessageLst:
            await messageMETA.channel.send('**Dood cookie? cookie what?** Now take this, idc - :cookie:')
            return

        if MessageLst[0].lower() in {'help', 'cmd', 'command'}: 

            embed_boi = discord.Embed(title="Command/Help", description="Shows the Commands and General overthrough of the Bot")
            embed_boi.add_field(name='cookie CoolGame', value='\ncookie CoolGame help\n cookie CoolGame init\n cookie CoolGame Terminate')
            embed_boi.add_field(name='cookie math <expression>', value='\nCan Solve Math expressions : presently +, -, *, /, ^ are supported.')

            await messageMETA.channel.send(content=None, embed=embed_boi)

        elif MessageLst[0] == 'math':
            MessageLst.remove('math')

            FinalPrint = MathCookie(MessageLst)

            await messageMETA.channel.send(f'\n <@{messageMETA.author.id}> ' + FinalPrint)

        elif MessageLst[0] == 'CoolGame':
            MessageLst.remove('CoolGame')

            if not MessageLst or MessageLst[0] == 'help':
                embed_boi = discord.Embed(title='CoolGame Cmds and Help', description=helpCoolGame())
                await messageMETA.channel.send(content=None, embed=embed_boi)
            elif MessageLst[0] == 'init':
                if messageMETA.author in PlayersRn:
                    await messageMETA.channel.send('Already initiatd!! UwU')
                    return
                PlayersRn.update({messageMETA.author : [RandomList(),None]})
                await messageMETA.channel.send(f'\n <@{messageMETA.author.id}> ' + 'Game has now initiated')
                print(PlayersRn[messageMETA.author][0])
            elif MessageLst[0].lower() == 'terminate':
                if messageMETA.author in PlayersRn:
                    await messageMETA.channel.send('Game terminted :frowning:')
                    PlayersRn.pop(messageMETA.author)
                    return
            else:
                embed_boi = discord.Embed(title='CoolGame Cmds and Help', description=helpCoolGame())
                await messageMETA.channel.send(content=None, embed=embed_boi)

client.run(TOKEN)   