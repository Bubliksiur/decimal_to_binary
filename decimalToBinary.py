def decimal_to_binary(n):
    result = ""
    while n > 0:
        last_digit = n % 2
        n = n // 2
        result = str(last_digit) + result
    return result

if __name__ == "__main__":
    print(decimal_to_binary(15))