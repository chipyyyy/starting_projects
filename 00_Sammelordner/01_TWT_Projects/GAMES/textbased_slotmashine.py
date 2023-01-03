import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4, 
    "C": 6, 
    "D": 10,
}

symbol_values = {
    "A": 5,
    "B": 4, 
    "C": 3, 
    "D": 10,
}

def check_winning(columns,lines,bet,values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns: 
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break 
        else: 
            winnings += values[symbol] * bet
    
    return winnings
            
def get_slotmachine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = [] 
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

#[['C', 'D', 'B'], ['A', 'B', 'C'], ['C', 'B', 'B']]

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns): #enumera() - nummeriert alle einrtäge von columns durch. Vereinfacht die counter.
            if i != len(col) - 1: #len(col)-1 ist das maximale Item in der Liste
                print(col[row], end = ' | ')
            else:
                print(col[row])

    print()

def deposit():
    while True:
        value = input('Was möchtest du einzahlen? €')
        if value.isdigit():
            value = int(value)
            if value > 0:
                break
            else: 
                print('Du kannst keine 0€ einzahlen.')
        else:
            print('Gib bitte eine Zahl ein.')

    return value

def get_number_of_lines():
    while True:
        lines = input('Auf wie viele Reihen möchtest du wetten? (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print('Du musst auf 1-3 Reihen wetten.')
        else:
            print('Gib bitte eine Zahl ein.')

    return lines

def get_bet():
    while True:
        bet = input('Wie viel möchtest du wetten? ')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else: 
                print(f'Du musst zwischen {MIN_BET} - {MAX_BET} wetten. ')
        else:
            print('Gib bitte eine Zahl ein.')

    return bet

def spin(balance):
    lines = get_number_of_lines() 
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance: 
            print(f'Du hast nicht genügend Geld für die Wette. Dein maximaler Einsatz ist: {balance}€')
            return 0
        else: 
            break 

    print(f'Du      hast {bet}€ auf {lines} Reihen gewettet. Gesamtwette: {total_bet}€')
    slots = get_slotmachine_spin(ROWS, COLS, symbol_count)     
    print_slot_machine(slots)
        
    winning = check_winning(slots, lines, bet, symbol_values)
    print(f'Du hast {winning}€ gewonnen! ')

    return winning - total_bet
    
def main():
    balance = deposit()
    while True:
        game = spin(balance)
        balance += game
        print(f'Aktueller Kontostand: {balance}€\n')
        answer = input('Press Enter to play (q to quit) ')
        if answer == 'q': 
            break 
    
    print(f'Du hast {balance}€ gewonnen. ')

    

main()



            
