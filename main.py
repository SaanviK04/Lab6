# Saanvi Kosiganti"s Encoder file


def decode(input):
    result = ""
    tempnum = 0
    for i in range(0, len(input)):  # for loop i in the given input
        tempnum = int(input[i])
        result += str((tempnum - 3))  # each individual decimal added to the result to get the result
    return result

menu_option = 1

while menu_option != 3:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')
    print('Please enter an option:')
    menu_option = int(input())

    if menu_option == 1:
        print('Please enter your password to encode:')
        og_password = str(input())
        encoded_password = ''
        place_value = 0

        while place_value < len(og_password):
            encoded_password += str( int(og_password[place_value]) + 3)
            place_value += 1
        print('Your password has been encoded and stored!')
        print('')


    elif menu_option == 2:  # subtracts 3 to each integer in the numeric string
        decoded_string = decode(og_password)
        print(f"The encoded password is {encoded_password}, and the original password is {og_password}.")
        print()










