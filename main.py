def binary_to_decimal(binary_str):
    value = 0
    for i in range(7,-1,-1):
        num = binary_str[7-i]
        if num == "1":
            value+=2**i
    return value

def decimal_to_binary(number):
    binary = ""
    exponent = 7
    for i in range(8):
        if number >= 2**exponent:
            binary+='1'
            number -= 2**exponent
        else:
            binary += '0'
        exponent -= 1
    return binary

