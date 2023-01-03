#Kaprekar-Konstante: Differenz aus größtgmöglicher und kleinstmöglicher Zahl, die aus 4 Zahlen gebaut werden können, konvergieren gegen die Kaprekar-Konstante
#Kaperkar-Konstante = 6174

import pandas as pd
import matplotlib.pyplot as plt

k = 6174


def find_smallest(n): 
    res_n = [int(x) for x in str(n)]
    res_n.sort()
    res_string = ''.join(str(x) for x in res_n)
    res_n = int(res_string)
    return res_n
    

def find_biggest(n): 
    res_n =[int(x) for x in str(n)]
    res_n.sort(reverse=True)
    res_string = ''.join(str(x) for x in res_n)
    res_n = int(res_string)
    return res_n

def i_kaperkar(n):
    i = 0
    while True:
        n_i = find_biggest(n)-find_smallest(n)
        i += 1
        if n_i == k:
            break
        elif n == 999: 
            n_i = 8991
            break
        elif n_i == 0: 
            return 0
        n = n_i
    return i

def main():
    plot_i_n = []
    for n in range(1000,9999+1):
       i_n = i_kaperkar(n)
       plot_i_n.append(i_n)
    print(plot_i_n)
    plot_n = [x for x in range(1000,9999+1)]
    print(plot_n)

    plt.scatter(plot_n, plot_i_n, marker='.')
    plt.show()
    

main()



