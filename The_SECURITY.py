print('NEW SCHOOL?')
print('I will guide you')
print('BUT FIRST, ANSWER MY QUESTIONS!')

name = input('WHATS YOUR NAME\n')
print('ALRIGHT', name.upper(), 'ANSWER THE FOLLOWING QUESTIONS')
print('AND I WILL GUIDE YOU TO YOUR NEW CLASS')
print()

cor = 0
answer = int(input('WHAT IS 3 + 70\n'))

if answer == 73 :
    print('LOOKS LIKE YOU DO HAVE A BRAIN!')
    print('I THOUGHT YOU DID NOT')
    cor = cor + 1
else :
    print('YOU SHOULD STUDY NURSERY FIRST!')
    print('I THOUGHT YOU WERE GRADE 7')
    print()

answer = input('WHAT STARTS WITH AN (N) AND ENDS WITH AN (N)\n')

if answer.startswith('n') and answer.endswith('n') :
    print('NICE TRY')
    print('ITS NOT A BIG DEAL THOUGH')
    cor = cor + 1
else :
    print('ITS SO EASY')
    print('THERE ARE SO MUCH')
    print('TAKE THE WORD( NOUN ) FOR AN EXAMPLE')
    print('YOU ARE WASTING MY TIME')
    print()

sentence = input('WRITE A SENTENCE USING THE WORD ( INEFFABLE)\n')

if 'ineffable' in sentence.lower() :
    print('EASY!')
    print('AT LEAST YOU TRIED')
    cor = cor + 1
else :
    print('GET OUT!')
    print('I SAID USE THE WORD ( INEFFABLE )')
    print()

print('LAST QUESTION!')
num = (input('WHAT IS 2,000 x 4,000\n'))

num = num.replace(',' , '')

if int(num) == 8000000 :
    print('WELL...')
    cor = cor + 1
    if cor < 4 :
        print('Y0U ARE NOT ACCEPTABLE FOR THIS SCHOOL')
        print('YOU COULD NOT EVEN ANSWER THOSE EASY QUESTONS!')
    else:
        print('I GUESS YOU COULD JOIN THE SCHOOL')

        for i in range (100) :

            sec = input('WHICH SECTION ARE YOU |A|B|C|D|\n')

            if sec.upper() == 'A' :
                print('WARNING! SHE MIGHT BE WORKING RIGHT NOW!')
                break

            elif sec.upper() == 'B' :
                print('YOU NEED TO GO ALL THE WAY UPSTAIRS!')
                break

            elif sec.upper() == 'C' :
                print('CAUTION, THEY MIGHT BE DOING AN ACTIVITY!')
                break

            elif sec.upper() == 'D' :
                print('OH, YOU ARE NEXT TO THE GRADE 6 STUDENTS!')
                break

            else :
                print('IM SORRY!')
                