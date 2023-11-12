def log_function_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Called {func.__name__} with {args} and got result {result}")
        return result
    return wrapper

@log_function_call
def multiply(a, b):
    return a * b

multiply(5, 3)


import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Executing {func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@timing_decorator
def sample_function(num):
    sum = 0
    for i in range(num):
        sum += i
    return sum

# Calling the decorated function
print(sample_function(1000000))
