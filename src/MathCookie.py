import random


def random_list():
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


def check_integer(num: str, if_decimal: bool):
    if num == '':
        return False
    cnt = 0
    for i in num:
        if i == '.':
            cnt += 1
            if cnt == if_decimal+1:
                return False 
        elif i < '0' or '9' < i:
            return False

    return True


def best(string_as_number):
    if string_as_number[0] == '.':
        string_as_number = '0' + string_as_number
    elif string_as_number[-1] == '.':
        string_as_number += '0'

    return string_as_number


def infix_to_postfix(inf):
    stack = []
    postfix_list = []
    for j in inf:
        if check_integer(j, True):
            postfix_list.append(best(j))
        elif j == '(':
            stack.append('(')
        elif j == ')':
            while stack[-1] != '(' and stack:
                postfix_list.append(stack[-1])
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
                    postfix_list.append(stack[-1])
                    try:
                        stack.pop()
                    except IndexError:
                        return None
                stack.append(j)
        
    while stack:
        postfix_list.append(stack[-1])
        try:
            stack.pop()
        except IndexError:
            return None
    return postfix_list


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
    return int(a) % int(b)


def arithmetic(func, a, b):
    return func(a, b)


function_name = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
    '^': exponent,
    '%': modulo
}


def evaluate(postfix_list):
    stack = []
    for j in postfix_list:
        if check_integer(j, True):
            stack.append(j)
        else:
            try:
                one = float(stack[-1])
                stack.pop()
                two = float(stack[-1])
                stack.pop()
            except (ValueError, IndexError):
                return None
            try:
                stack.append(str(arithmetic(function_name[j], two, one)))
            except ZeroDivisionError:
                return None
    answer = float(stack[-1])
    return answer


def string_to_infix_list(inf):
    cache = ''
    final_infix_list = []
    for c in inf:
        if c == ' ':
            if cache != '':
                final_infix_list.append(cache)
                cache = ''
        elif '0' <= c <= '9' or c == '.':
            cache += c
        elif c in {'+', '-', '*', '/', '^', '(', ')', '%'}:
            if cache != '':
                final_infix_list.append(cache)
                cache = ''
            final_infix_list.append(c)
        else:
            return None
    if cache != '':
        final_infix_list.append(cache)

    return final_infix_list


def expression_processor(infix_string):
    infix_string = infix_string.replace('modulo', '%').replace('mod', '%').replace('[', '(')
    infix_string = infix_string.replace(']', ')').replace('{', '(').replace('}', ')')
    infix_list = string_to_infix_list(infix_string)
    if not infix_list:
        return None
    postfix_list = infix_to_postfix(infix_list)

    if not postfix_list:
        return None

    return evaluate(postfix_list)


def random_between(start: int, end: int) -> int:
    return random.randint(start, end)


def math_cookie(infix_list):
    if not infix_list:
        return None

    answer = expression_processor(' '.join(infix_list))

    if (not answer) and answer != 0:
        return None

    answer = round(answer, 4)

    return answer
