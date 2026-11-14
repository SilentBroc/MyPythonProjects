
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

menu = ['A stolen diamond', 'real shiny gold', 'Time machine', 'Ps6',
        'pineapple pizza', 'Explosive potato', 'milk before the cereal',
        'money printer']

price = [80.00, 79.75, 200.00, 150.00, 15.50, 100.00, 21.50, 311.75]

print('_____________________________________________________')
print('ZA ITEMS'.ljust(30), 'ZA PRICE')
print('_____________________________________________________')
print()
print()

for kk in range(len(menu)):
    print(str(kk+1) + '.' + menu[kk])
    print('item'.ljust(30), str(price[kk]) + '$')

print('_____________________________________________________')
print()

shopping_cart = []
shopping_amount = []

shopping_comp = False



while not shopping_comp:

    order = int(input('PLEASE TYPE IN 1-8 TO SELECT YOUR ITEMS, 9 TO CHECKOUT\n'))

    if 1 <= order <= 8:

        print('PURCHASING', menu[order-1])

        quant = int(input('how many do you wannna add\n'))

        if quant <= 0:
            print('PLEASE ENTER A VALID QUANTITY')

        elif menu[order-1] in shopping_cart:

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




confirm = False
discount_applied = False

while not confirm:

    grand_tot = 0.0

    print()
    print('YOUR SH0PPING CART')

    print('__________________________________________________________________________________')
    print('ZA ITEMS'.ljust(30), 'ZA QUANTITY'.ljust(30), 'ZA PRICE')
    print('__________________________________________________________________________________')

    for kk in range(len(shopping_cart)):

        idx = menu.index(shopping_cart[kk])
        unit_price = price[idx]

        total_price = round(unit_price * shopping_amount[kk], 2)
        grand_tot += total_price

        print(shopping_cart[kk].ljust(30),
              str(shopping_amount[kk]).ljust(30), total_price)

    grand_tot = round(grand_tot, 2)

    print()
    print('Your total amount is', grand_tot)

    confirmation = input('ARE Y0U SURE YOU WANT TO BUY\n TYPE 1 IF YES\n TYPE 2 IF NO\n')

    if confirmation == '1':

        print('ALRIGHT, UR ORDER WILL BE DELIVERED IN TWO DAYS SINCE YOU LIVE IN', region)

        discount = input('Do you want to add a discount? (Y/N)\n')

        if discount.upper() == 'Y':

            print('you can get a (10%) discount if you buy for 1000$ since its the birthday of Illegon today')

            if grand_tot >= 1000 and not discount_applied:

                print('ADDING DISCOUNT...')

                discount_amount = round(grand_tot * 0.10, 2)
                grand_tot = round(grand_tot - discount_amount, 2)

                discount_applied = True

                print('YOU HAVE ADDED A (10%) DISCOUNT TO YOUR CART')
                print('YOUR TOTAL NOW IS', grand_tot)

            elif grand_tot < 1000:

                print('Your total is not 1000$ yet')
                print('PLEASE ADD MORE ITEMS TO YOUR SHOPPING CART')

                shopping_comp = False

                while not shopping_comp:

                    order = int(input('PLEASE TYPE IN 1-8 TO SELECT YOUR ITEMS, 9 TO CHECKOUT\n'))

                    if 1 <= order <= 8:

                        print('PURCHASING', menu[order-1])

                        quant = int(input('HOW MANY DO YOU WANT TO ADD?\n'))

                        if quant > 0:

                            if menu[order-1] in shopping_cart:

                                idx = shopping_cart.index(menu[order-1])
                                shopping_amount[idx] += quant

                            else:

                                shopping_cart.append(menu[order-1])
                                shopping_amount.append(quant)

                        else:
                            print('INVALID QUANTITY!')

                    elif order == 9:

                        shopping_comp = True

                    else:

                        print('INVALID INPUT!')

                continue

        elif discount.upper() == 'N':

            print('OK, NO DISCOUNT ADDED')

        else:

            print('INVALID DISCOUNT OPTION')
            continue

        answer = input('ARE YOU SURE YOU WANT TO CHECKOUT (Y/N)\n')

        if answer.upper() == 'Y':

            print('YOUR ORDER HAS BEEN PLACED')
            print('THANK YOU FOR SHOPPING AT ILLEGON!')
            confirm = True

        elif answer.upper() == 'N':

            print('You have cancelled your order')
            print('PEACE OUT!')
            confirm = True

        else:

            print('INVALID')

    elif confirmation == '2':

        print('H0PE YOU HAVE A NICE DAY')
        print('PEACE OUT!')

        confirm = True

    else:

        print('INVALID!')