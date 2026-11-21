print('Hello')
print('Welcome to the missing operator game')
print('In this game, I will find out how smart you are')
user = input('May I know ur name please\n')

print('Hey', user)
print('Lets start the game')

import random
for i in range(0,3) :

    num1 = int(input('PLEASE give me a number without any decimals. Anything but 0!\n'))
    num2 = int(input('PLEASE give me another number without any decimals. Without 0!\n'))

    op = random.randint(0, 2)

    if op == 0:
        rhs = num1 + num2

    elif op == 1:
        rhs = num1 - num2

    elif op == 2:
        rhs = num1 * num2

    op_list = ['+', '-', '*']


    print('Can you tell me the missing operator:')

    qn_format = str(num1) + ' __ ' + str(num2) + ' = ' + str(rhs) + '\n'
    answer = input(qn_format)

    if answer == op_list[op]:
        print('Well Done')
        
    else:
        print('WORK HARDER MATE!')
        
        i = i+1
        print(i)
        op1 = random.randint(0, 2)
        op2 = random.randint(0, 2)
        

        if op1 == 0:

            rhs = num1 + num2
        if op1 == 1:

            rhs = num1 - num2
        if op1 ==2 :
            rhs = num1 * num2


        qn_format = str(num1) + ' __ ' + str(num2)+' = ' + str(rhs) + '\n'
        answer = input(qn_format)

        if answer == op_list[op1] :
       # if answer[0] == op_list[op1] and answer[1] == op_list[op2]:

            print('Well done')
            # print(i)
        else:

            print('PATHETIC!!!')
           
    
    play = int(input('DO YOU WANT TO PLAY AGAIN ???\n TYPE 1 : YES\n TYPE 2 : NO''\n'))

    if play == 1 and i == 2:
        print('SORRY ALL YOUR ATTEMPTS ARE OVER')