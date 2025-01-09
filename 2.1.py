
def check(number):
    if number < 0:
        return "Negative number"
    elif number == 0:
        return "Neither prime nor composite"
    elif is_prime(number):
        return "Prime number"
    else:
        return "Composite number"

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

try:
    user_input = int(input("Please enter a number"))
    result = check(user_input)
    print(result)

except ValueError:
    print("Invalid input! Please enter a valid number.")