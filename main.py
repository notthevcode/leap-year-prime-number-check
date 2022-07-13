# ____________________________Leap Year Check____________________________

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("that's not a number you dumbfuck, please enter a valid number")
            continue
        else:
            break

    return value


user_input_leap = get_valid_input(
    "Enter a year to check whether it's a leap year or not: ")


def check_leap_year(user_input_leap):
    if user_input_leap % 400 == 0 or user_input_leap % 100 != 0 and user_input_leap % 4 == 0:
        print(f"{user_input_leap} is a leap year!")

    else:
        print(f"{user_input_leap} is not a leap year!")


check_leap_year(user_input_leap)

# ____________________________Prime Number Check____________________________

user_input_prime = get_valid_input(
    "Enter a number to check whether it's a prime number or not: ")


def prime_checker(user_input_prime):
    if user_input_prime > 1:
        for i in range(2, int(user_input_prime/2)+1):
            if user_input_prime % i == 0:
                print(f"{user_input_prime} is not a prime number!")
                break
        else:
            print(f"{user_input_prime} is a prime number!")

    else:
        print(f"{user_input_prime} is not a prime number!")


prime_checker(user_input_prime)
