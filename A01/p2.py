# Solve the problem from the second set here
"2. The palindrome of a number is the number obtained by reversing the order of its digits (e.g. the palindrome of 237 is 732). For a given natural number n, determine its palindrome."


def main():
    number = int(input("type your number: "))
    pal = 0
    while number !=0:
        pal = number % 10 + pal * 10  # we simply write the number in inverse order in a new variable by starting with last digit, ... until the first digit

        number = number // 10
    print(pal)


main()

""" another way

def main():
    number=input("type any number: ")
    print(number[::-1])  


main()

"""
