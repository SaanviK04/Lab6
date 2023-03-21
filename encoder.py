
## Saanvi Kodiganti's Encoder File

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

    elif menu_option == 2:









