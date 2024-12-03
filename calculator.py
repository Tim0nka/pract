def summa(item, result):
    return item + result

def sub(item2, result):
    return item2 - result
   

def mult(item3, result):
    return item3 * result
    

def div(item4, result):
     return item4 / result
    

user_input = input('Введите пример: ')


if '+' in user_input:
    user_input_list = user_input.split('+')
    result = float(user_input_list[0])
    for i in range (1,len(user_input_list)):
        user_input_list[i]=float(user_input_list[i])
        result = summa(user_input_list[i],result)
    print(result)


if '-' in user_input:
    user_input_list = user_input.split('-')
    result = float(user_input_list[0])
    for i in range (0,len(user_input)):
        user_input_list[i]=float(user_input_list[i])
        result = sub(user_input_list[i],result)
    print(result)

if '*' in user_input:
    user_input_list = user_input.split('*')
    result = float(user_input_list[0])
    for i in range (0,len(user_input)):
        user_input_list[i]=float(user_input_list[i])
        result = mult(user_input[i],result)
    print(result)

if '/' in user_input:
    user_input_list = user_input.split('/')
    result = float(user_input_list[0])
    for i in range (0,len(user_input)):
        user_input_list[i]=float(user_input_list[i])
        result = div( result,user_input[i])
    print(result)