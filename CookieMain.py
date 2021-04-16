import os

import discord
from dotenv import load_dotenv

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


def CheckInteger(num):
    cnt = 0
    for i in num:
        if i == '.':
            cnt += 1
            if cnt == 2:
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
        if CheckInteger(j):
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
        if CheckInteger(j):
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


@client.event
async def on_message(messageMETA):
    if messageMETA.author == client.user:
        return

    MessageLst = messageMETA.content.split()

    if MessageLst[0] == 'cookie':
        MessageLst.remove('cookie')

        if not MessageLst:
            await messageMETA.channel.send('**Dood cookie? cookie what?** Now take this, idc - :cookie:')
            return

        if MessageLst[0] == 'math':
            MessageLst.remove('math')

            if not MessageLst:
                await messageMETA.channel.send('Incorrect expression? At least get your shit right man')
                await messageMETA.channel.send(':pensive:')
                return

            Answer = ExpressionProcessor(' '.join(MessageLst))

            if Answer == None:
                await messageMETA.channel.send('Incorrect expression? At least get your shit right man')
                await messageMETA.channel.send(':pensive:')
                return
            
            await messageMETA.channel.send('Nice there you go, Your expression yieldeth : ' + '**' + f'{Answer}' + '**')
            return
    else:
        return

client.run(TOKEN)   