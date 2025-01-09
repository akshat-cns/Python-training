class MathOperations:
    def add(self, a, b):
        if isinstance(a, list) and isinstance(b, list):
            return [x + y for x, y in zip(a, b)]
        return a + b

    def subtract(self, a, b):
        if isinstance(a, list) and isinstance(b, list):
            return [x - y for x, y in zip(a, b)]
        return a - b

    def matrix_multiply(self, mat1, mat2):
        if len(mat1[0]) != len(mat2):
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second.")
        
        result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)] for row in mat1]
        return result


if __name__ == "__main__":
    math_ops = MathOperations()

    print(''' \nChoose an operation:
    1. Addition
    2. Subtraction
    3. Matrix multiplication
    4. List all books
    5. Exit ''')
    
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(f"The result of addition is: {math_ops.add(a, b)}")
    elif choice == 2:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(f"The result of subtraction is: {math_ops.subtract(a, b)}")
    elif choice == 3:
        print("Enter the first matrix (row by row, space-separated):")
        rows1 = int(input("Number of rows: "))
        mat1 = [list(map(int, input().split())) for _ in range(rows1)]
        
        print("Enter the second matrix (row by row, space-separated):")
        rows2 = int(input("Number of rows: "))
        mat2 = [list(map(int, input().split())) for _ in range(rows2)]
        
        try:
            result = math_ops.matrix_multiply(mat1, mat2)
            print("The result of matrix multiplication is:")
            for row in result:
                print(row)
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice!")
