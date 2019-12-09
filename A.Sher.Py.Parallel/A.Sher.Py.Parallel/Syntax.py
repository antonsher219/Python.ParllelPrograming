#однорядковий коментарі починаються зі знаку "#"

"""багатострокові коментарі починаються
та закінчуються 
трьома подвійними лапками"""

#Импортування модулів та їх окремих функцій

import math

from math import sqrt, fabs, ceil, floor

def printSyntaxInfo():
    
    print("-----Syntax Info-----")
    # ----- Основні оператори та конструкції

    #Оператор присвоювання: =
    int5 = 5
    int6 = 6

    #Операторы порівняння

    print("int5 = 5; int6 = 6\n")

    print("int5 == int6: ", end='')
    print(int5 == int6) # == False
    print("int5 != int6: ", end='')
    print(int5 != int6) # != True

    print("int5 > int6: ", end='')
    print(int5 > int6) # > False
    print("int5 < int6: ", end='')
    print(int5 < int6) # < rue

    print("int5 >= int6: ", end='')
    print(int5 >= int6) # >= False
    print("int5 <= int6: ", end='')
    print(int5 <= int6) # <= True

    print("int5 is int6: ", end='')
    print(int5 is int6) # is False
    print("int5 is not int6: ", end='')
    print(int5 is not int6) #is not True

    #Оператор збільшення значення змінної: +=

    int5 += 1
    print("\nint5 += 1; int5 = %d\n" % int5)

    #Оператор зменшення значення змінної: -=

    int5 -= 1
    print("\nint5 -= 1; int5 = %d\n" % int5)

    #Умовні оператори 

    print("\nif operator result:")
    if int5 == 5:
        print("int5 == 5")
    elif int5 == 0:
        print("int5 == 0")
    else:
        print("int5 != 5")
    
    print("\nelse operator result:")
    if int5 != 5: print("int5 == 5")
    else: print("int5", end=''); print(" != ", end=''); print("5\n\n")

    #звичайна конструкція if else:
    X = True
    Y = "X is True"
    Z = "X is False"
    A = ""

    if X:
        A = Y
    else:
        A = Z

    print(A)

    #скороченый запис конструкції
    X = False
    A = Y if X else Z

    print(A)

def forCycle():
    print()
    print("-----For Cycle-----")
    for i in 'hello world':
        print(i * 2, end='')
    print()

def whileLoop():
    print()
    print("-----While Loop-----")
    i = 5
    while i < 15:
        print(i)
        i = i + 2
    print()

def listInfo():
    print()
    print("-----List info-----")
    
    empty = []  #Пустий список. Створюється за допомогою квадратних скобок []
    print("Пустий список")
    print(empty)
    
    print()

    notEmpty = ['s', 'p', ['isok'], 2]
    print("Непустий дворівневий список")
    print(notEmpty)

    #Генерація списку зі строки "word" за допомогою for. 
    #До кожного элементу послідовності буде застосовано конструкції, вказану в квадратних скобках
    
    print()

    print("Сгенерований список")
    generatedList = [char * 3 for char in 'word']
    print(generatedList)

def cutterInfo():    
    print()
    print("-----Cutter info-----")
    #item[START:STOP:STEP] - бере зріз від номеру START, до STOP (не включаючи його), с шагом STEP
    #також можливе звернення до элементів з від'ємним індексом. Тоді відлік буде йти з кінця послідовності. seq[-1] поверне останній елемент
    #можна приміняти до будь-якої послідовності - список, строка і т.д.

    a = [num for num in range(1, 10)]
    
    print("a")
    print(a)

    print("a[:]")
    print(a[:])

    print("a[-1]")
    print(a[-1])

    print("a[:-1]")
    print(a[:-1])

    print("a[-1:5:-1]")
    print(a[-1:5:-1])

    print("a[::-1]")
    print(a[::-1])

    print()


def tupleInfo():
    print()
    print("-----Tuple info-----")
    #Пустий кортеж. Створюється за допомогою круглих скобок () або функції tuple().
    #На відміну від кортежів, він є незмінним. 
    #Покласти новий елемент або змінити його довжину буде неможливо.
    empty = ()
    #або
    empty = tuple()

    print("Пустий кортеж")
    print(empty)
    
    print("Заповнений кортеж")
    notEmpty = ('t', ['u', 'p'], ('l', 'e'), 0)
    print(notEmpty)

    #Якщо в кортежі є елемент, що можна змінити, то Ви не отримаєте винятку.
    #Проте, якщо Ви заміните будь-який елемент, це викличе виняткову ситуацію - Exception
    print("Заповнений кортеж(змінено)")
    notEmpty[1][0] = 'd'
    print(notEmpty)





def main():
    printSyntaxInfo()
    forCycle()
    whileLoop()

    listInfo()
    cutterInfo()
    tupleInfo()


main()

    