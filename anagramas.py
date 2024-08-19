# la idea es poder (i) hacer anagramas desde X palabra y (ii) poder comparar X y Y palabras para verificar si son anagramas
import random, os, math
from collections import Counter
from itertools import permutations

def calc_anagramas(str3): #fx permutations de chat - no he entendido al 100 pero simplifica todo y resuelve issue de sort:
    # Generar todas las permutaciones posibles de las letras de la palabra
    permutaciones = set(permutations(str3))
    # Convertir cada permutación de tupla a cadena
    anagramas = {''.join(p) for p in permutaciones}
    return anagramas

def anagramas2(str3):
    str3 = str3.replace(' ', '').lower()
    anagramas = calc_anagramas(str3)
    print(f"\nLos anagramas posibles para la palabra '{str3}' son:\n")
    for anagrama in sorted(anagramas): print(anagrama)

def anagramas1(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    if len(str1) != len(str2): return False
    else: 
        str1_sorted = sorted(str1)
        str2_sorted = sorted(str2)
        return str1_sorted == str2_sorted

def run():
    while 1:
        menu = int(input('\nANAGRAMAS\n\n1.Generar anagrama\n2.Verificar anagrama\n3.Salir\n\nElige una opción:'))
        if menu == 1:
            os.system('clear')
            str3 = input('GENERAR ANAGRAMAS\n\nInserta palabra inicial:\n\n')
            anagramas2(str3)
        elif menu == 2:
            os.system('clear')
            print('¿ES ANAGRAMA?\n\nInserta 2 palabras')
            str1 = input('\npalabra 1:\n')
            str2 = input('\npalabra 2:\n')
            print(f'\n{anagramas1(str1,str2)}\n\n***')
        elif menu == 3: break
        else: 
            os.system('clear')
            menu = print('Ingresa una opción válida:')

if __name__ == '__main__': run()