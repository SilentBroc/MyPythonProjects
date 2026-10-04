import random
attempts = 0


print('CHOOSE YOUR JOB')
print('A = THEIF')
print('B = ORDINARY MAN')

job = input('WHO DO YOU WANNA BE?\n')

if job.upper() == 'A' :
    print('HELLO FELLOW THEIF')
    name = input('WHAT IS YOUR NAME?\n')

    print('HELL0', name.upper())
    print('I HOPE YOU ARE READY F0R YOUR FIRST MISSION')
    print('THIS MISSION WILL PUT YOUR SKILLS TO THE TEST')

    print('THIS MISSION IS A BANK ROBBERY')
    print('YOU HAVE TO UNLOCK A LOCKER AND GET TONS OF MONEY')
    print('I TRUST YOU WITH THIS MISSION')
    print()
    print()
    print()
    print()
    print('LATER THAT DAY...')
    print()
    print()
    print('WE ARE HERE!')
    print('NOW GUESS THE CODE FROM 1 TO 99')
    theif = False

    num = random.randint(1 , 99)
  
    while not theif :
        guess = int(input('WHAT IS YOUR GUESS\n'))

        if guess > num :
            print('THE CODE IS SMALLER')
            attempts = attempts + 1
        elif guess < num :
            print('THE CODE IS LARGER')
            attempts = attempts + 1
        elif guess == num :
            print('WHAT!')
            if attempts > 7 :
                print('YOU HAVE LOCKED THE LOCKER')
                print('YOU ONLY GET 7 ATTEMPTS!')
                theif = True
            else :
                print('NO WAY!')
                print('YOU ARE A GENIUS')
                print('YOU UNLOCKED THAT IN', attempts, 'ATTEMPTS')
                print('I HAVE NOT BEEN ABLE TO UNLOCK THAT LOCKER FOR YEARS!')
                print('YOOU...')
                print()
                print("██     ██   ██████   ██    ██   ██")
                print("██     ██  ██    ██  ███   ██   ██")
                print("██  █  ██  ██    ██  ██ ██ ██   ██")
                print("██ ███ ██  ██    ██  ██  ████ ")
                print(" ███ ███    ██████   ██   ███   ██")
                theif = True

else :
    print('HELL0 USER')
    print('TO SET A CODE FOR Y0UR LOCKER...')
    print('YOU MUST ANSWER THE FOLLOWING QUESTOINS!')
    name = input('PLEASE ENTER YOUR NAME HERE\n')
    money = input('PLEASE ENTER HOW MUCH MONEY YOU HAVE\n')
    
    print('HELLO', name.upper())
    print('LETS START')
    
    cor = 0
    
    answer = int(input('GIVE ME A NUMBER THAT IS BETWEEN 50 AND 70\n'))

    if answer < 70 and answer > 50 :
        print('THAT WAS NOTHING\n')
        cor = cor + 1
    else:
        print('HOW COULD YOU SET A CODE LIKE THIS\n')

    print('next QUESTION')

    print('THE FURIOUS LION TRIED TO HUNT HIS DELICIOUS PREY WHILE THE COLD BREEZE BLEW')
    answer = input('IDENTIFY 3 ADJECTIVES FROM THIS STATEMENT\n')

    if answer.upper().count('FURIOUS') and answer.upper().count('DELICIOUS') and answer.upper().count('COLD') :
        print('SO YOU ARE NOT IN KINDERGARTEN')
        print('WHATEVER!\n')
        cor = cor + 1
    else :
        print('OH MY GOSH!',name.upper())
        print('YOU ARE IN KINDERGARTEN ARENT YOU?')
        print('YOU DID NOT FIND ALL THE ADJECTIVES!')
        print('URGH, YOU ARE WASTING MY TIME!')
        print('ANYWAYS...\n')

    print('LAST QUESTION')

    answer = input('WHAT HAPPENS WHEN HYDROGEN AND OXYGEN ARE MIXED TOGETHER?\n')

    if answer.upper() == 'WATER' :
        cor = cor + 1
        print('WELL..')
        if cor == 3 :
            print('I GUESS YOU COULD MAKE YOUR OWN CODE!')
            code = input('PLEASE WRITE YOUR CODE HERE\n')
            print('THANK YOU')
            print('YOU MAY LEAVE THIS BANK WITH CONFIDENCE')
            print('WE WILL KEEP YOUR PASSWORD SAFE')
            print('YOU CAN TEST YOUR LOCK RIGHT NOW IF YOU WANT!')
            lock = input('please enter code here\n')
            if lock == code :
                print('HELLO', name.upper(), 'YOUR MONEY IS HERE:', money)
            else :
                print('INTRUDER!')
    
    else :
        print('I AM SORRY...')
        print('BUT YOU DO NOT HAVE THE MATURITY TO CREATE YOUR OWN LOCK')
        print('SEE YOU WHEN YOU ARE 18 YEARS 0LD')