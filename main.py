def sum_of_odd_digits(n = 110550099):
    total_sum = 0
    for digit in str(n):
        digit = int(digit)
        if digit % 2 != 0:
            total_sum += digit
    return total_sum

sum = sum_of_odd_digits()
print("sum = " + str(sum))