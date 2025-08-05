#if number is positive
def digit_sum(num):
    if num < 10:
        return num
    if num >= 10:
        sum = 0
        num = str(num)
        for i in range(len(num)):
            sum += int(num[i])
        return sum

#print(digit_sum(105))

#second approach
def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

print(sum_digits(222))

#recursive technique

def digits_of_sum(n):
    if n ==0:
        return 0
    else:
        return n%10 + digits_of_sum(n // 10)

print(digits_of_sum(22))

