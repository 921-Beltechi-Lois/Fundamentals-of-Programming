# Solve the problem from the third set here
"""
3. Generate the largest perfect number smaller than a given natural number n. If such a number does not exist, a message should be displayed.
A number is perfect if it is equal to the sum of its divisors, except itself. (e.g. 6 is a perfect number, as 6=1+2+3).
"""

def divisors(x): # finds the sum of its divisors

    s=0
    for i in range(1,x):
        if x%i==0: s=s+i       # sum is calculated if we find its own divisor
    if(s==x): return 1         # perfect number found
    return 0

def find_perf_number(x):           # this is an intermediate function that says if we find / or not the given number
    while divisors(x)==0:          # when this condition is true --> we successfully found our perfect number and we return it
        if x<0: return "we couldn't find any perfect number"        # our perfect number needs to be natural
        x=x-1                                                       # we didn't previously find any perfect number, so we decrease the given number
        divisors(x)
    return x                       # perfect number found

def main():
    number=int(input("enter any number: "))
    find_perf_number(number)
    print("the result is: ", find_perf_number(number - 1))

main()