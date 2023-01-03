import random as rd 


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

#Gibt den Zahlenbereich in dem gerechent werden soll zurück
def zahlenbereich():
    while True:
        left_in = input('Gib die Grenzen der ersten Zahl ganzzahlig ein (Zahl,Zahl)\n')
        try:
            left_in = [int(i) for i in left_in.split(',')]
        except: 
            print('Deine Eingabe ist falsch!')
            continue
        if len(left_in) > 2: 
            print('Du musst genau zwei Zahlen eingeben!\n')
        elif any(n < 0 for n in left_in):
            print('Du kannst keine negatiben Zahlen eingeben!\n')
        elif left_in[0] > left_in [1]:
            print('Das ist kein gültiger Zahlenbereich!\n')
        else:
            break    

    while True:
        right_in = input('Gib die Grenzen der zweiten Zahl ganzzahlig ein (Zahl,Zahl)\n')
        try: 
            right_in = [int(i) for i in right_in.split(',')]
        except:
            print('Deine Eingabe ist flasch!')
            continue
        if len(right_in) > 2: 
            print('Du musst genau zwei Zahlen eingeben!\n')
        elif any(n < 0 for n in right_in):
            print('Du kannst keine negatiben Zahlen eingeben!\n')
        elif right_in[0] > right_in [1]:
            print('Das ist kein gültiger Zahlenbereich!\n')
        else:
            break

    left_a = left_in[0]
    left_b = left_in[1]
    right_a = right_in[0]
    right_b = right_in[1]

    zb_left = [zahl for zahl in range(left_a,left_b+1)]
    zb_right= [zahl for zahl in range(right_a, right_b+1)]

    return zb_left, zb_right

#Fragt die Rechenarten ab, die geübt werden sollen
def get_rechenarten():
    rechenarten = []
    available = {1:'Additon', 2:'Subtraktion', 3:'Multiplikation',4:'Divison'}

    while True:
        print('\nWas möchtest du üben?\n')
        for num, rechenart in zip(available.keys(), available.values()): #Gibt die noch vorhanden Rechenarten aus
            print(f'{num} {rechenart}')
        eingabe = input('\nGib die Recheanrten ein, die du üben möchtest. \n')
        if eingabe.isdigit(): 
            if 1 <= int(eingabe) <= 4 and int(eingabe) not in rechenarten:
                rechenarten.append(int(eingabe)) #Hier vermutlich besser noch ein weiteres dict anzulegen und die Werte dort drin zu speichern
                available.pop(int(eingabe))
            else: 
                print('Deine Eingabe ist ungültig probiere es nochmal!')
        else:
            print('Deine Eingabe ist ungültig probiere es nochmal!')
        
        if not bool(available): #checks if dict is empty. Empty dicts evaluates to False in Python
            break

        more = input('Möchtest du noch mehr Rechenarten üben? Enter=ja, q=quit\n')
        if more == 'q':
            break

    return rechenarten

#Erstellt das Problem und überprüft bei Division ob solvable()
def problem(rechenarten, zb_left, zb_right):
    rechenart = rd.choice(rechenarten)
    num1 = rd.choice(zb_left)
    num2 = rd.choice(zb_right)
    rechenarten_out = {1:'+', 2:'-', 3:'*', 4:'/'}
    #Überprüft, ob Division ganzzahlig ist.
    if rechenart == 4:
        while not divide(num1, num2).is_integer():
            num1 = rd.choice(zb_left)
            num2 = rd.choice(zb_right)
    
    problem = f'{num1} {rechenarten_out[rechenart]} {num2}'
    print(problem)

    # String nach Operation auslesen
    if '+' in problem:
        solution = add(num1, num2)
    elif '-' in problem:
        solution = subtract(num1, num2)
    elif '*' in problem:
        solution = multiply(num1, num2)
    elif '/' in problem:
        solution = int(divide(num1, num2))

    return problem, solution


def rerun():
    eingabe = input('Enter for next problem! q to quit')
    if eingabe == 'q':
        return False
    else: 
            return True

def main():
    zb_left, zb_right = zahlenbereich()
    rechenarten = get_rechenarten()

    while True:
        problemset, solution = problem(rechenarten, zb_left, zb_right)

        while True:
            guess = input('Ergebnis: ')
            try: 
                if int(guess) == solution:
                    print(f' {solution} ist richtig!') #man könnte am Ende noch eine prozentualen Anteil der richtigen und falschen Ergebnisse angeben
                    break
                else: 
                    print('Falsch! Probier es nochmal!\n')
            except: 
                print('Deine Eingabe ist ungültig!\n')

        if not rerun():
            break

main()