def summa(first, second):

    return first + second


def sub(first, second):

    return first - second


def mult(first, second):

    return first * second


def div(first, second):

    return first / second

user_input = input('Введите пример: ')


if '+' in user_input:
    user_input_list = user_input.split('+')
    result = 0
    for i in range (0,len(user_input)):
        user_input_list[i]=float.user_input_list[i]
        result = summa( result,user_input[i])


if '-' in user_input:
    user_input_list = user_input.split('-')
    result = 0
    for i in range (0,len(user_input)):
        user_input_list[i]=float.user_input_list[i]
        result = sub( result,user_input[i])


if '*' in user_input:
    user_input_list = user_input.split('*')
    result = 0
    for i in range (0,len(user_input)):
        user_input_list[i]=float.user_input_list[i]
        result = mult( result,user_input[i])


if '/' in user_input:
    user_input_list = user_input.split('+')
    result = 0
    for i in range (0,len(user_input)):
        user_input_list[i]=float.user_input_list[i]
        result = div( result,user_input[i])


for i in range (0,len(user_input)):
    user_input[1]=float.user_input[i]
result = add( user_input[i],user_input[1])
print(result)


