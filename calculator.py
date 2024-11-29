def add(a,b):
    pass


user_input = input('Введите пример: ')

if '+' in user_input:
    user_input_list = user_input.split('+')
    result = 0
    for i in range (0,len(user_input)):
        user_input_list[i]=float.user_input_list[i]
        result = add( result,user_input[i])


user_input = user_input.split('*')
user_input = user_input.split('/')

for i in range (0,len(user_input)):
    user_input[1]=float.user_input[i]
result = add( user_input[i],user_input[1])
print(result)


