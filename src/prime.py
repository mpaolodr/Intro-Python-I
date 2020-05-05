# UNDERSTAND
# number given on command line - command line arg?
# Prime number?
# only divisors are 1 and itself
# cannot be factored
# number greater than 1


# PLAN

# We need sys module for command line args
# Have an empty list to store divisors
# Divide number by 1 to number itself plus 1 (range(2, number + 1))
# if result is int append to list
# if list length is greater than 2, number is composite


# EXECUTE

import sys

# grab number from cmd line arg
number = sys.argv[1]


def is_prime(num=2):
    divisors_list = [1]

    for divisor in range(2, (int(num) + 1)):
        result = int(num) / divisor

        if result.is_integer() == True:
            divisors_list.append(int(divisor))
        else:
            pass

    if len(divisors_list) > 2:
        print(divisors_list)
        print("Composite Number")
    else:
        print(divisors_list)
        print("Prime Number")


is_prime(number)
