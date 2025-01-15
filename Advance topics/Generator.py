def fib(start, end):
    a, b = 0, 1
    for i in range(end):  
        if i >= start:   
            yield a
        a, b = b, a + b


start_ind = int(input("Enter the start : "))
end_ind = int(input("Enter the end : "))
for num in fib(start_ind, end_ind):
    print(num, end=" ")