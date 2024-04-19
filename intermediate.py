def rotate_character(input_char, shift_value):
    if input_char == " ":
        return input_char
    else:
        alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        char_index = alphabet_list.index(input_char)
        adjusted_index = (char_index + shift_value) % 26
        shifted_char = alphabet_list[adjusted_index]
        return shifted_char

def shift_message(input_message, shift_value):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    shifted_message = ""
    
    for char in input_message:
        if char == " ":
            shifted_message += char
        else:
            char_index = alphabet.index(char)
            adjusted_index = (char_index + shift_value) % 26
            shifted_message += alphabet[adjusted_index]
        
    return shifted_message

def adjust_character_by_letter(input_char, shift_char):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    shift_value = alphabet.index(shift_char)
    
    if input_char == " ":
        return input_char
    else:
        char_index = alphabet.index(input_char)
        adjusted_index = (char_index + shift_value) % 26
        shifted_char = alphabet[adjusted_index]
        return shifted_char
    
def key_based_cipher(input_message, cipher_key):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    extended_key = (cipher_key * (len(input_message) // len(cipher_key))) + cipher_key[:len(input_message) % len(cipher_key)]
    ciphered_message = ""
    

    for i, char in enumerate(input_message):
        if char == " ":
            ciphered_message += " "
        else:
            letter_shift = extended_key[i]
            shift_value = alphabet.index(letter_shift)
            char_index = alphabet.index(char)
            adjusted_index = (char_index + shift_value) % 26
            shifted_char = alphabet[adjusted_index]
            ciphered_message += shifted_char
    
    return ciphered_message

def encode_with_scytale(input_message, rotation):
    if len(input_message) % rotation != 0:
        input_message += '_' * (rotation - len(input_message) % rotation)
    
    ciphered_message = ''
    for i in range(len(input_message)):
        ciphered_message += input_message[(i // rotation) + (len(input_message) // rotation) * (i % rotation)]
    
    return ciphered_message

def decode_with_scytale(input_message, rotation):
    rows = len(input_message) // rotation
    deciphered_chars = []
    for row in range(rows):
        for col in range(rotation):
            index = col * rows + row
            deciphered_chars.append(input_message[index])
    deciphered_message = ''.join(deciphered_chars)
    deciphered_message = deciphered_message.rstrip('_')
    return deciphered_message
