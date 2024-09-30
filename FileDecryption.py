flipped_codes = {
    '!': 'A', '@': 'a',
    '#': 'B', '$': 'b',
    '%': 'C', '^': 'c',
    '&': 'D', '*': 'd',
    '(': 'E', ')': 'e',
    '-': 'F', '+': 'f',
    '=': 'G', '~': 'g',
    '{': 'H', '}': 'h',
    '[': 'I', ']': 'i',
    ':': 'J', ';': 'j',
    '<': 'K', '>': 'k',
    '?': 'L', '/': 'l',
    '1': 'M', '2': 'm',
    '3': 'N', '4': 'n',
    '5': 'O', '6': 'o',
    '7': 'P', '8': 'p',
    '9': 'Q', '0': 'q',
    '|': 'R', '`': 'r',
    '"': 'S', "'": 's',
    'A': 'T', 'B': 't',
    'C': 'U', 'D': 'u',
    'E': 'V', 'F': 'v',
    'G': 'W', 'H': 'w',
    'I': 'X', 'J': 'x',
    'K': 'Y', 'L': 'y',
    'M': 'Z', 'N': 'z',
    'O': ' ', 'P': '.',
    'Q': '?', 'R': "'",
    'S': '!', 'T': '@',
    'U': '#', 'V': '$',
    'W': '&', 'X': '(',
    'Y': ')', 'Z': '-',
    'a': '%', 'b': ',',
    'c': ':', 'd': ';'
}


infile = open('encrypted.txt', 'r')

reader = infile.read()

for letter in reader:
    if letter in flipped_codes:
        print(flipped_codes[letter],end='') #find the encrpyted code's key in dictionary and print its value and repeat without going to a newline

    
infile.close()
