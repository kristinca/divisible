"""

A simple program to check if some input elements of a list
         are divisible by some input integer
          without using the modulo operator,

"""
from dataclasses import dataclass
import sys
from typing import List


def nasterisk(n):
    """ A function that returns n asterisks """

    return(int(n) * '*')


def div1(num1, num2):
    """
    A simple function to check if an input integer is divisible by another input integer
                        without using the modulo operator
    """
    try:
        first_number = num1
        second_number = num2
        answer = int(first_number) / int(second_number)
        if answer.is_integer():
            print(f'\nThe number {first_number} is divisible by the number {second_number},'
                  f'the result is : {int(answer)}.')
        else:
            print(f'\nThe number {first_number} is not divisible by the number {second_number}.')

    except ZeroDivisionError:
        """ We handle the ZeroDivisionError """
        m1 = ' Zero division! '
        print(f"\n{nasterisk(len(m1))}\n{m1}\n{nasterisk(len(m1))}")

    except ValueError:
        """ We handle the ValueError """
        m2 = ' At least one of the numbers is not an integer! '
        print(f"\n{nasterisk(len(m2))}\n{m2}\n{nasterisk(len(m2))}")


def fin(s):
    """ A simple function to end the program when entered 'q' """

    if s == 'q':
        sys.exit()
    pass



def msginfo():
    """ A simple output messages to be printed when handling exceptions """
    m1 = ' Inappropriate argument type or inappropriate argument value! '
    m2 = " Enter 'q' to exit. "
    print(f'\n{nasterisk(len(m1))}\n{m1}\n{nasterisk(len(m1))}')
    print(f"\n{nasterisk(len(m2))}\n{m2}\n{nasterisk(len(m2))}")



while True:
    """ The program ends by entering 'q' """
    try:
        m1 = ' S T A R T '
        print(f'\n {nasterisk(len(m1))}{m1}{nasterisk(len(m1))} \n')
        list1 = []
        n1 = input('\nEnter the number of elements in the list...\t')
        fin(n1)
        if int(n1) <= 0:
            msginfo()
        else:
            for i in range(0, int(n1)):
                list1.append(input(f'\nEnter the element with index value {i} ... \t'))
            for elem in list1:
                if '[' == str(elem)[0] and ']' == str(elem)[len(str(elem))-1]:
                    elem = list(elem)
                    print('aaaaaaaaaaaaaaa list fooouuunnndd! :D')
                elif '(' == str(elem)[0] and ')' == str(elem)[len(str(elem)) - 1]:
                    elem = tuple(elem)
                    print('aaaaaaaaaaaaaaa tuple fooouuunnndd! :D')
                # elif '{' == str(elem)[0] and '}' == str(elem)[len(str(elem)) - 1]:
                #     elem = dict(elem)
                #     print('aaaaaaaaaaaaaaa dictionary fooouuunnndd! :D')
            n2 = input(f"\nEnter the number of elements you want to check for divisibility from list {list1}"
                 f" or enter 'q' to exit...\t")
            fin(n2)
            if int(n2) <= 0 or int(n2) > len(list1):
                continue
            else:
                n3 = []
                for i in range(0, int(n2)):
                    n3.append(input('\nEnter the index of the element to check for divisibility...\t'))
                # check if there are lists, tuples or dictionaries among the chosen elements
                # for i in str(list(dict.fromkeys(n3))):
                #     if isinstance(list1[i], list) or isinstance(list1[i], tuple):
                #         print('ok')
                #     else:
                #         continue
                #     if '[' and ']' in str(i) or '(' and ')' or ('{' and '}') in str(i):
                #         print(f'A list, a tuple or a dictionary in {list1} has been found. ')
                # #         it works ok, to do ...
                d = input("\nEnter the divisor or enter 'q' to exit...\t")
                fin(d)
                try:
                    for j in list(dict.fromkeys(n3)):
                        # isinstance not working !!!
                        if isinstance(list1[int(j)], int):
                            div1(int(list1[int(j)]), int(d))
                        elif isinstance(list1[int(j)], (list, tuple)):
                            for num in list1[int(j)]:
                                div1(int(num), int(d))
                except IndexError:
                    m3 = f" There is no element with index {j} in {list1} "
                    print(f'\n{nasterisk(len(m3))}\n{m3}.\n{nasterisk(m3)}\n')
                except TypeError:
                    m4 = f" Inappropriate argument type: {list1[j]}. "
                    print(f'\n{nasterisk(len(m4))}\n{m4}\n{nasterisk(m4)}\n')
                except ValueError:
                    m5 = f" Inappropriate argument value: {list1[j]}. "
                    print(f'\n{nasterisk(len(m5))}\n{m5}\n{nasterisk(len(m5))}\n')
                print("\nEnter 'q' to exit.")
                continue
    except TypeError:
        msginfo()
        continue
    except ValueError:
        msginfo()
        continue

#
# def proveriint(i):
#     if isinstance(i, int):
#         print('ok')
#
#
# l1 = [6, 7, 'guidhgdi', ('ytry', 6, 8.9, [3, 4, [4, 'gfdgd']]), ['rewrew', 9778, -2.364]]
#
#
# def flatPrint(myList):
#     for thing in myList:
#         if isinstance(thing, list) or isinstance(thing, tuple):
#             flatPrint(thing)
#         else:
#             print(thing)
#
# flatPrint(l1)

# for elem in l1:
#     if isinstance(elem, int):
#         print(elem)
#     else:
#         for elem1 in elem:
#             if isinstance(elem1, int):
#                 print(elem1)
#             else:
#                 for elem2 in elem1:
#                     if isinstance(elem2, int):
#                         print('iii')
#                     else:
#                         print(f'e2   {elem2}')