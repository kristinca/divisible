"""

A simple program to find
the non-repeating elements and their indexes in an input list

"""

import listdiv


def non_repeat_el(l1):
    """ A function that returns the non-repeating elements
    and their indexes in a list """

    l3 = l1.copy()
    el_non_repeat = []
    non_repeat_index = []
    l2 = list(dict.fromkeys(l1))
    for num in l2:
        l3.remove(num)
        if num not in l3:
            non_repeat_index.append(l1.index(num))
            el_non_repeat.append(num)
    if len(el_non_repeat) > 0:
        print(f'Non-repeating elements from the list{l1}:\n {el_non_repeat}, their indexes: {non_repeat_index}')
    else:
        print(f'There are no non-repeating elements in the list {l3}')


def main():
    pass


if __name__ == "__main__":
    while True:
        """ The program ends by entering q """
        try:
            listdiv.startmsg()
            list1 = []
            n1 = input("\nEnter the number of elements in the list or enter q to exit...\t")
            listdiv.fin(n1)
            if int(n1) <= 0:
                listdiv.msginfo()
            else:
                list1 = listdiv.inputel(n1)
                non_repeat_el(list1)

        except TypeError:
            listdiv.msginfo()

        except ValueError:
            listdiv.msginfo()

        except IndexError:
            listdiv.msginfo()