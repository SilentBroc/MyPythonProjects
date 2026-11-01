print()
print()

print('WELCOME TO ILLEGON')
print('THIS STORE IS DEFINITELY NOT AN ILLEGAL STORE')
print('PLEASE SIGN UP TO START SHOPPING')
print()

user = input('What is your username\n')
region = input('Type in your region below\n')
age = int(input('Please type in your age below to show recommended items for you\n'))

print('Hello', user)
if age <= 11:
    print('Here are the following items we recommend for you kid')
else:
    print('Here are the following items we recommend sir')

menu = ['A stolen diamond', 'real shiny gold', 'Time machine', 'Ps6', 'pineapple pizza', 'Explosive potato', 'milk before the cereal', 'money printer']
price = [80.00, 79.75, 200.00, 150.00, 15.50, 100.00, 21.50, 311.75]

print('_____________________________________________________')
print('ZA ITEMS'.ljust(30), 'ZA PRICE excl tax')
print('_____________________________________________________')
print()
print()

for kk in range(len(menu)):
    print(str(kk+1)+'.'+menu[kk])
    print('item'.ljust(30), str(price[kk])+'$')
print('_____________________________________________________')
print()

shopping_cart = []
shopping_amount = []

shopping_comp = False

while not shopping_comp:
    order = int(input('PLEASE TYPE IN 1-8 TO SELECT YOUR ITEMS, 9 TO CHECKOUT\n'))

    if order <= 8:
        print('PURCHASING', menu[order-1])
        quant = int(input('how many do you wannna add\n'))

        if menu[order-1] in shopping_cart:
            print('repeated the purchase')
            idx = shopping_cart.index(menu[order-1])
            shopping_amount[idx] += quant
        else:
            print('new purchase')
            shopping_cart.append(menu[order-1])
            shopping_amount.append(quant)

    elif order == 9:
        print('PR0CEEDING TO CHECK0UT...')
        shopping_comp = True

    else:
        print('INVALID INPUT!')

print()    
print('YOUR SH0PPING CART')

grand_tot = 0.0

print('__________________________________________________________________________________')
print('ZA ITEMS'.ljust(30), 'ZA QUANTITY'.ljust(30), 'ZA PRICE')
print('__________________________________________________________________________________')

for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price = price[idx]
    total_price = round(unit_price*shopping_amount[kk], 2)
    grand_tot += total_price

    print(shopping_cart[kk].ljust(30) , str(shopping_amount[kk]).ljust(30) , total_price)
    
grand_tot = round(grand_tot, 2)
print()
print()
print('Your total amount is', grand_tot)

confirm = False

while not confirm:
    
    confirmation = int(input('ARE Y0U SURE YOU WANT TO BUY\n TYPE 1 IF YES\n TYPE 2 IF NO\n'))
    
    if confirmation == 1:
        print('ALRIGHT, UR ORDER WILL BE DELIVERED IN TWO DAYS')
        print('KA - CHING')
        print('Transaction is done')
        print('PEACE OUT DUDE')
        confirm = True
    
    elif confirmation == 2:
        print('H0PE YOU HAVE A NICE DAY')
        print('PEACE OUT!')
        confirm = True
    
    else:
        print('INVALID!')