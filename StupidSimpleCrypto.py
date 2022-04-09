

# Simple crypto for exercise work
def simple_encrypt():
    message = input('Message?: ')
    number_list = []
    for letter in message:
        number_list.append(ord(letter)-(ord('a') - 1))
    print(number_list)


def simple_decrypt():
    # input number
    cypher = input('Cypher? :')
    # check if even or odd length
    if len(cypher) % 2 != 0:
        # if odd add a leading 0
        cypher = '0' + cypher

    # split list into 2 digit integers
    cypher_list = []
    for
    # convert each integer to a corresponding letter
    # print result




def main():
    print('Stupid Simple Crypto')
    while True:
        crypto_function = input("Encrypt, Decrypt, or Quit")
        if crypto_function == 'e':
            simple_encrypt()
        elif crypto_function == 'd':
            simple_decrypt()
        elif crypto_function == 'q':
            break
        else:
            print('I don\'t understand')
    print('Goodbye')


main()
