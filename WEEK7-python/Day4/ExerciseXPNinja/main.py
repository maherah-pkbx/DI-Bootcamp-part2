"""
Exercise 1 : What’s Your Name ?
Instructions
Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.
"""


def get_full_name(first_name, last_name, middle_name=""):
    if len(middle_name) > 0:
        return f'{first_name} {middle_name} {last_name}'
    else:
        return f'{first_name} {last_name}'


print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))








"""
Exercise 2 : From English To Morse
Instructions
Write a function that converts English text to morse code and another one that does the opposite.
Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.
"""

morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    1: '.----', 2: '..---', 3: '...--', 4: '....-', 5: '.....', 6: '-....', 7: '--...', 8: '---..', 9: '----.',
    0: '-----', ',': '--..--', '?': '..--..', ':': '---...', '-': '-....-', '"': '.-..-.', '(': '-.--.', '=': '-...-',
    '*': '-..-', '.': '.-.-.-', ';': '-.-.-.', '/': '-..-.', "'": '.----.', '_': '..--.-', ')': '-.--.-', '+': '.-.-.',
    '@': '.--.-.'
}


def eng_to_morse(string):
    word_list = string.split(' ')
    encoded_letters = []
    
    for word in word_list:
        for char in word:
            encoded_letters.append(morse_code[char.lower()])
        encoded_letters.append(' ') # Add a space between each word.

    return ' '.join(encoded_letters)


def morse_to_eng(string):
    morse_list = string.split(' ')
    print(morse_list)

    decoded_letters = []
    for letter in morse_list:
        if letter == '':
            decoded_letters.append(' ')
        for k, v in morse_code.items():
            if v == letter:
                decoded_letters.append(k)

    return ''.join(decoded_letters)


print(eng_to_morse('Sending out an SOS'))
print(morse_to_eng(eng_to_morse('Sending out an SOS')))


