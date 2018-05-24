hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# simple python solution:
# hex_str_decode = hex_str.decode('hex')
# hex_str_encode = hex_str_decode.encode('base64')
# print hex_bytes

# understanding hex:
# hex_test = '6d'
# result = 13 + 6*16
# print hex_test.decode('hex')

base64_str = ''
hex_alphabet = {'a': 10,
                'b': 11,
                'c': 12,
                'd': 13,
                'e': 14,
                'f': 15,
                'g': 16}

# loop through hex string and write to bytes
while not hex_str == '':
    # take first two digits of hex code
    hex_tuple = hex_str[:2]
    # erase first two digits of hex code
    hex_str = hex_str[2:]
    ascii_sum = 0
    # decode first digit
    hex_one = hex_tuple[1]
    if hex_one in hex_alphabet:
        ascii_sum = hex_alphabet[hex_one]
    else:
        ascii_sum = int(hex_one)
    # decode second digit
    hex_two = hex_tuple[0]
    if hex_two in hex_alphabet:
        ascii_sum += hex_alphabet[hex_two]*16
    else:
        ascii_sum += int(hex_two)*16
    # debug: print ascii_sum, chr(ascii_sum)

    # write ascii_sum to byte (not necessary for solution of challenge)
    single_byte = ascii_sum.to_bytes(1, byteorder='big', signed=True)
    print("{0:b}".format(ascii_sum))

    # convert ascii_sum to base64
    # lazy solution
    base64_str += str(ascii_sum).encode('base64')


