

# Simple crypto for exercise work
def simple_encrypt():
    message = input('Message?: ')
    number_list = []
    for letter in message:
        number_list.append(ord(letter)-(ord('a') - 1))
    print(number_list)


def simple_decrypt():
    cypher = input('Cypher? :')
    if len(cypher) % 2 != 0:
        cypher = '0' + cypher
    cypher_list = [int(cypher[index:index + 2]) for index in range(0, len(cypher), 2)]
    letter_list = []
    for code in cypher_list:
        letter_list.append(chr(code + ord('a') - 1))
    print(cypher_list)
    word = ''
    print(word.join(letter_list))


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
