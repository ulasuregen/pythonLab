def rotatedDigits(n: int) -> int:
    valid = 0
    valid_digits = [2,5,6,9]
    invalid_digits = [3,4,7]

    for i in range(1,n+1):
        valid_B = False
        while i > 0:
            print(i)
            res = i % 10
            if res in valid_digits:
                valid_B = True
            elif res in invalid_digits:
                valid_B = False
                break
            i //= 10

        valid += valid_B

    return valid

res = rotatedDigits(10)
print(res)