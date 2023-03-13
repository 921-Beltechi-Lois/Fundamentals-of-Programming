""" A2
 - read a complex number from the console
 - write a complex number to the console,
 - implement each required functionality

Use a list, tuple or dictionary tu represent each complex number (e.g. 1-2i as [1, -2], (1, -2) or {'real': 1, 'imag': -2} respectively).
To access or modify numbers, use getter and setter functions.

Separate input/output functions (those using print and input statements) from those performing the calculations (see program.py)

Input data should be read from the console and the results printed to the console


1. Read a list of complex numbers (in z = a + bi form) from the console.
2. Display the entire list of numbers on the console.
3. Display on the console the longest sequence that observes a given property. Each student will receive 2 of the properties from the list provided below.
4. Exit the application


Specifications for the functions related to point 3 above.
10 complex numbers already available at program startup.


The sequence (consists of):

8. The modulus of all elements is in the [0, 10] range. Modulus: sqrt(a^2+b^2) >0 && <10

12. Both real and imaginary parts can be written using the same base 10 digits (e.g. 1+3i, 31i, 33+i, 111, 11-313i)

"""

#
# Write the implementation for A2 in this file
#

# TODO UI section
# (write all functions that have input or print statements here).
# Ideally, this section should not contain any calculations relevant to program functionalities
# print('Hello A2')
# Function section
# --------------------------------------------------------------

import math

def read_complex_number_ui(complex_number_list):
    # TODO Crash if values cannot be converted to an integer, or in case of empty string
    real_part = int(input("Real part: "))
    img_part = int(input("Imaginary part: "))
    complex_number = create_complex_number(real_part, img_part)
    result = add_complex_number(complex_number_list, complex_number)
    if not result:
        print('Duplicate number - cannot add complex number')


def print_menu():
    print("1. Read a complex number (in z = a + bi form) from the console.")
    print("2. Display the entire list of numbers on the console.")
    print("3. Display on the console the longest sequence that observes a given property.")
    print("4. Exit the application")


def print_list_ui(complex_number_list):
    for complex_number in complex_number_list:
        print(str(get_real_part(complex_number)) + '+' + str(get_img_part(complex_number)) + '*i')


def check_modulus_list_ui(complex_number_list):
    modulus_list = get_modulus_list(complex_number_list)
    print(modulus_list)


def check_10base_digits_ui(complex_number_list):
    longest_sequence = get_longest_sequence_with_same_base_digits(complex_number_list)
    print('')
    print_list_ui(longest_sequence)


# (write all NON-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values
# print('Hello A2'!) -> prints aren't allowed here!


def get_real_part(complex_number):
    return complex_number['real']


def get_img_part(complex_number):
    return complex_number['imaginary']


def check_base_digits(complex_number_list, i):
    """

    :param complex_number_list: List of complex numbers
    :param i: Positions of the complex numbers list : CURRENT & PREVIOUS complex numbers are together verified
    :return: TRUE = ordered digit list of previous NO. == ordered digit list of current NO.\
                OR 0 appears in one of the list (any number can be written as 0* that number)\
             FALSE = both of the complex numbers couldn't be written using the same base 10 digits
    """
    previous_digits = get_digits_list(complex_number_list, i - 1)
    current_digits = get_digits_list(complex_number_list, i)
    return current_digits == previous_digits or 0 in current_digits or 0 in previous_digits


def get_longest_sequence_with_same_base_digits(complex_number_list):
    """
    Both real and imaginary parts can be written using the same base 10 digits (e.g. 1+3i, 31i, 33+i, 111, 11-313i)
    We're finding the longest sequence that respects this property

    :param complex_number_list: List of complex numbers
    :return: A LIST with longest sequence of complex numbers that has numbers written in same 10 base digits
    """
    first = -1
    dim = -1
    max_dim = -1
    p1 = -1
    p2 = -1
    for i in range(1, len(complex_number_list)):
        if check_base_digits(complex_number_list, i):    # current and previous complex numbers are compared: i=1
            if first == -1:
                first = i - 1
                dim = 2
            else:
                dim = dim + 1
        else:
            if dim > max_dim:
                max_dim = dim
                p1 = first
            first = -1
            dim = -1
    if dim > max_dim:
        max_dim = dim
        p1 = first
    if max_dim != -1:
        p2 = p1 + max_dim - 1
        result = []
        for i in range(p1, p2 + 1):
            result.append(complex_number_list[i])
        return result
        # return complex_number_list[p1:p2]
    return []


def get_digits_list(complex_number_list, i):
    """

    :param complex_number_list: List of complex numbers
    :param i: Position
    :return: LIST of sorted 'complex_number_digits' of a given complex number from the complex number list on position i
    """
    complex_number = complex_number_list[i]
    complex_number_digits = get_complex_number_digits(complex_number)
    complex_number_digits.sort()   # sort !!
    return complex_number_digits


def get_complex_number_digits(complex_number):
    """
    We extract from a given complex number its own digits; those digits are concatenated; in order to get away of duplicated digits we put 'em in a set;
    :param complex_number: Given complex number
    :return: A LIST of complex number's digits with NO duplication (real & img part both together written) which were stored in a set
    """
    real_part = get_real_part(complex_number)
    img_part = get_img_part(complex_number)

    real_digits = get_number_digits(real_part)
    img_digits = get_number_digits(img_part)

    return list(set(real_digits + img_digits))


def get_number_digits(number):
    """
    We store in digits LIST all digits of the given number
    :param number: Given part of complex number
    :return: LIST of 'digits' that stores all its own number digits (duplicated too)
    """
    number = abs(number)
    digits = []
    if number == 0:
        return [0]
    while number != 0:
        digits.append(number % 10)
        number = number // 10
    return digits


def check_modulus(complex_number):
    """

    :param complex_number: Given complex number
    :return: TRUE = value of the modulus complex number is in the range [0,10], otherwise FALSE
    """
    real = get_real_part(complex_number)
    img = get_img_part(complex_number)
    value = math.sqrt(real * real + img * img)
    if value >= 0 and value <= 10:
        return 1  # modulus good to go
    return 0


def get_modulus_list(complex_number_list):
    """
    :param complex_number_list: All complex number list
    :return: Returns the LIST of modulus numbers found in longest sequence (list called "result"), if no match -> then the list is empty
    """
    first = -1
    dim = -1
    max_dim = -1
    p1 = -1
    p2 = -1
    length = int(len(complex_number_list))
    for i in range(length):
        if check_modulus(complex_number_list[i]):  # true
            if first == -1:
                first = i
                dim = 1
            else:
                dim = dim + 1
        else:
            if dim > max_dim:
                max_dim = dim
                p1 = first
            first = -1
            dim = -1
    if dim > max_dim:
        max_dim = dim
        p1 = first
    if max_dim != -1:
        p2 = p1 + max_dim - 1
        result = []
        for i in range(p1, p2 + 1):
            result.append(complex_number_list[i])
        return result
        # return complex_number_list[p1:p2]
    return []


def add_complex_number(complex_number_list, complex_number):
    """
    Add a complex number to the list of complex numbers
    :param complex_number_list: Complex numbers list
    :param complex_number: New complex number instance
    :return: True if complex number successfully added, False otherwise
    """
    if check_duplicity(complex_number, complex_number_list):
        return False
    else:
        complex_number_list.append(complex_number)
        return True


def check_duplicity(new_complex_number, complex_number_list):
    """
    :param new_complex_number: New added complex number with real & imaginary part
    :param complex_number_list: List of the complex numbers
    :return: True = number is duplicated, False  = number is NOT duplicated
    """
    for complex_number in complex_number_list:
        if get_real_part(new_complex_number) == get_real_part(complex_number) \
                and get_img_part(new_complex_number) == get_img_part(complex_number):
            return True  # number is duplicated
    return False


def create_complex_number(complex_number_real, complex_number_img):
    """
    We generate our complex numbers
    :param complex_number_real: Real part
    :param complex_number_img: Img part
    :return: Complex number stored in a dictionary, or error if input is a string
    """
    return {'real': complex_number_real, 'imaginary': complex_number_img}


def generate_complex_number_list():
    """
    Generates complex numbers (10 complex numbers already available at program startup)
    :return: the list of the complex numbers
    """
    return [
        create_complex_number(1, 3),
        create_complex_number(0, 31),
        create_complex_number(33, 1),
        create_complex_number(111, 0),
        create_complex_number(11, -313),
        create_complex_number(6, 5),
        create_complex_number(2, 3),
        create_complex_number(3, 2),
        create_complex_number(8, 2),
        create_complex_number(9, 1)
    ]


def main():
    complex_number_list = generate_complex_number_list()   # x 10 already generated
    while True:
        print_menu()
        option = input("Enter option = ")
        if option == '1':
            read_complex_number_ui(complex_number_list)
        elif option == '2':
            print_list_ui(complex_number_list)
        elif option == '3':
            property = input(" 8 = modulus of complex numbers\n 12 = same 10-base-digits\n Property number: ")
            if property == '8':
                check_modulus_list_ui(complex_number_list)
            elif property == '12':
                check_10base_digits_ui(complex_number_list)
        elif option == '4':
            return
        else:
            print("Invalid option!")


main()