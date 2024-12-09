
def factorial(n):
    i = 1
    result = 1
    if (n == 0) | (n == 1):
        result = 1
    else:
        while i < n:
            result = result * (i + 1)
            i = i + 1
    return result

if (factorial(0) == 1) & (factorial(1) == 1):
    print("No errors.")
    