#Write a function to calculate the square root of a number

def sqrt(n):
    result = 1
    for i in range(1, n//2 + 1):
        if i * i <= n:
            result = i
        else:
            break
    return result


#implementation here
print(sqrt(64))

