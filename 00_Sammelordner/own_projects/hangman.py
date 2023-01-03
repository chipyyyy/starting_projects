

def eingabe():
    while True: 
        suchwort = input('Gib ein Wort ein: ')
        if not suchwort.isalpha():
            print("Du darfst nur Buchstaben eingeben und keine Leerzeichen!")
        else: 
            break
    suchwort_list = list(suchwort)
    return suchwort_list


def get_letter(letterlist):
    while True:
        guess = input('Welchen Buchstaben möchtest du raten? ')
        if guess in letterlist:
            print('Den Buchstaben hast du schon erraten! ')
        elif len(guess) != 1:
            print('Du darfst nur einen Buchstaben raten!')
        else: 
            break
    return guess


def main():
    while True:
        letterlist = []
        wort = eingabe()
        
        for i in range(10):
            print('\n')

        name = input('Gib deinen Namen ein: ')
        code_wort = [' _ ' for i in wort]
        print(''.join(code_wort),'\n')
        
        while True:
            guess = get_letter(letterlist)
            letterlist.append(guess)
            for buchstabe in range(len(wort)):
                if guess == wort[buchstabe]: 
                    code_wort[buchstabe] = guess
            if code_wort == wort:
                print(f'Großartig {name}! Du hast das Wort erraten. Das Wort ist:', ''.join(wort))
                print()
                break
            else: 
                print(''.join(code_wort), f'Geratene Buchstaben: {letterlist}')
                print()
        next_round = input('Möchtest du nochmal spielen (Enter)? (q to quit)')
        if next_round == 'q':
            break

main()