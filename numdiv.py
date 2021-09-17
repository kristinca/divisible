"""
A simple program to check if an input integer is divisible by another input integer
                    without using the modulo operator
"""

import listdiv


def main():
    pass


if __name__ == "__main__":

    print("Enter 'q' to exit.")

    while True:
        """ The program ends by entering q """

        try:
            """ We input the first and second number and check if they are integers """
            listdiv.startmsg()
            first_number = input("\nEnter the first number or enter q to exit...\t ")
            listdiv.fin(first_number)
            second_number = input("\nEnter the first number or enter q to exit...\t ")
            listdiv.fin(second_number)
            answer = int(first_number) / int(second_number)
            if answer.is_integer():
                print(f'The number {first_number} is divisible by the number {second_number},'
                      f'the result is : {int(answer)}.')
            else:
                print(f'The number {first_number} is not divisible by the number {second_number}.')
            print("\nEnter 'q' to exit.")

        except ZeroDivisionError:
            """ We handle the ZeroDivisionError """

            print('Zero division!')
            print("\nEnter 'q' to exit.")

        except ValueError:
            """ We handle the ValueError """

            print('At least one of the numbers is not an integer!')
            print("\n Enter 'q' to exit.")