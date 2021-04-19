import random

def RandomList():
    first10 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while first10[0] == '0':
        random.shuffle(first10)
    return [first10[i] for i in range(4)]

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '%':
        return 2
    elif operator == '*':
        return 3
    elif operator == '/': 
        return 4
    elif operator == '^':
        return 5
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
                try:
                    stack.pop()
                except IndexError:
                    return None
            try:
                stack.pop()
            except IndexError:
                return None
        elif j == '^':
            stack.append('^')
        else:
            if stack and precedence(j) >= precedence(stack[-1]):
                stack.append(j)
            else:
                while stack and precedence(j) < precedence(stack[-1]):
                    PostfixList.append(stack[-1])
                    try:
                        stack.pop()
                    except IndexError:
                        return None
                stack.append(j)
        
    while stack:
        PostfixList.append(stack[-1])
        try:
            stack.pop()
        except IndexError:
            return None
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

def modulo(a, b):
    return int(a)%int(b)


def Arth(func, a, b):
    return func(a, b)

function_name = {
    '+' : addition,
    '-' : subtraction,
    '*' : multiplication,
    '/' : division,
    '^' : exponent,
    '%' : modulo
}

def evaluate(PostfixList):
    stack = []
    for j in PostfixList:
        if CheckInteger(j, True):
            stack.append(j)
        else:
            try:
                one = float(stack[-1])
                stack.pop()
            except (ValueError, IndexError):
                return None
            try:
                two = float(stack[-1])
                stack.pop()
            except (ValueError, IndexError):
                return None
            stack.append(str(Arth(function_name[j], two, one)))
    answer = float(stack[-1])
    return answer


def stringToInfixList(inf):
    cache = ''
    FinalInfixList = []
    for c in inf:
        if c == ' ':
            if cache != '':
                FinalInfixList.append(cache)
                cache = ''
        elif '0' <= c <= '9' or c == '.':
            cache += c
        elif c in {'+', '-', '*', '/', '^', '(', ')','%'}:
            if cache != '':
                FinalInfixList.append(cache)
                cache = ''
            FinalInfixList.append(c)
        else:
            return None
    if cache != '':
        FinalInfixList.append(cache)
        cache = ''
    return FinalInfixList


def ExpressionProcessor(InfixString):
    InfixString = InfixString.replace('modulo', '%')
    InfixString = InfixString.replace('mod', '%')
    InfixString = InfixString.replace('[', '(')
    InfixString = InfixString.replace(']', ')')
    InfixString = InfixString.replace('{', '(')
    InfixString = InfixString.replace('}', ')')
    InfixList = stringToInfixList(InfixString)
    if not InfixList:
        return None
    PostfixList = InfixtoPostix(InfixList)

    if not PostfixList:
        return None

    return evaluate(PostfixList)


def RandomBtwn(start: int, end: int) -> (int):
    return random.randint(start, end)


def MathCookie(InfixLst):
    if not InfixLst:
        return 'Incorrect expression? At least get your shit right man :pensive:'

    Answer = ExpressionProcessor(' '.join(InfixLst))

    if Answer == None:
        return 'Incorrect expression? At least get your shit right man :pensive:'

    Answer = round(Answer, 4)

    return 'Nice there you go, Your expression yieldeth : ' + '**' + f'{Answer}' + '**'