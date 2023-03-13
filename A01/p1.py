# Solve the problem from the first set here
""" 1. Generate the first prime number larger than a given natural number n."""


def check_prime_number(nr):
    if nr < 2:                                  # numbers smaller than 2 are not considered prime numbers
        return 0
    if nr == 2:                                 # 2 is considered a prime number
        return 1
    for i in range(2, nr // 2):
        if nr % i == 0:                         # if the number is dividing exactly, then prime number presumption is false
            return 0
    return 1                                    # we found a prime number, so we return true


def find_prime_greater_x(x):                    # this function is searching continuously until a prime number is found
    while check_prime_number(x) == 0:           # when this condition is true-> searching stops -> then we'll return the prime number
        x = x + 1                               # we didn't previously find any prime number, so we increase the given number
    return x


def main():
    x = int(input("Enter any number > 1: "))
    print("the result is: ", find_prime_greater_x(x + 1))   # x+1 - we're searching numbers greater than given number


main()
