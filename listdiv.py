"""

A simple program to check if some input elements of a list
         are divisible by some input integer
          without using the modulo operator

"""

import sys


def nasterisk(n):
    """ A function that returns n asterisks """

    return(int(n) * '*')

def fin(s):
    """ A simple function to end the program when entered 'q' """

    if s == 'q':
        sys.exit()
    pass


def inputel(n):
    """ A simple function to input the n - number of elements to be checked for divisibility """

    l = []
    for i in range(0, int(n)):
        l.append(input(f"\nEnter the element with index {i}...\t"))
        fin(i)
    return l


def list_in_list_el(l):
    """ A simple function to get all the numbers from a list into a new list
    including the elements of list within a list """
    # we enter the elements of list within a list with comma
    # don't use [] or ()

    for num0 in range(0, len(l)):
        if "," in l[num0]:
            l[num0] = l[num0].split(",")

    l2 = []
    for num1 in l:
        if isinstance(num1, (list, tuple)):
            for num2 in num1:
                l2.append(num2)
        else:
            l2.append(num1)
    return l2

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
        if int(n1) <= 0:
            msginfo()
        else:
            list1 = inputel(n1)
            # for i in range(0, int(n1)):
            #     list1.append(input(f'\nEnter the element with index value {i} ... \t'))
            # for elem in list1:
            #     if '[' == str(elem)[0] and ']' == str(elem)[len(str(elem))-1]:
            #         elem = list(elem)
            #         print('aaaaaaaaaaaaaaa list fooouuunnndd! :D')
            #     elif '(' == str(elem)[0] and ')' == str(elem)[len(str(elem)) - 1]:
            #         elem = tuple(elem)
            #         print('aaaaaaaaaaaaaaa tuple fooouuunnndd! :D')
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
                d = input("\nEnter the divisor or enter 'q' to exit...\t")
                fin(d)
                list2 = []
                for elem in list(dict.fromkeys(n3)):
                    list2.append(list1[int(elem)])
                list3 = []
                list3 = list_in_list_el(list2)
                for element in list3:
                    div1(int(element), d)
                print("\nEnter 'q' to exit.")

    except TypeError:
        msginfo()
        continue

    except ValueError:
        msginfo()
        continue