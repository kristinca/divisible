"""
A simple program to check if an input integer is divisible by another input integer
                    without using the modulo operator
"""

print("Enter 'q' to exit.")

while True:
    """ The program ends by entering q """

    try:
        """ We input the first and second number and check if they are integers """

        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        if second_number == 'q':
            break
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