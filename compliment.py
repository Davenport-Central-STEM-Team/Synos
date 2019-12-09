def signed_int_to_hex(input=0):

    number = int(input)

    if number < 0:
        number += (1 << 8)
        hexValue = hex(number)
        return hexValue
    elif number >= 0:
        hexValue = hex(number)
        return hexValue
    else:
        pass

while True:
    number = input("Enter a number, you dumb fuck!")

    print(signed_int_to_hex(number))