import time
from functools import wraps

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)  
        end_time = time.time()  
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds")
        return result  
    return wrapper

@log_execution_time
def process_large_dataset(data):
    total = 0
    for num in data:
        total += num
    return total

large_data = range(1, 10000000)

result = process_large_dataset(large_data)
print(f"Result: {result}")
