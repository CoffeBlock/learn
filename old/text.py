def fibonacci(num):  
    if num == 1:
        return 1
    elif num == 0:
        return 0
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(13))