inputs = [int(i) for i in input().split()]

def multiply_numbers(*args):
    product = 1

    for num in args:
        if isinstance(num, (int, float)):
            product *= num
        else:
            print(f"Error: '{num}' is not a valid number.")
            return None

    return product

result = multiply_numbers(*inputs)
if result is not None:
    print(f"The product is: {result}")

