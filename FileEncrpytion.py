import csv
codes = { 
    'A': '!',   'a': '@',
    'B': '#',   'b': '$',
    'C': '%',   'c': '^',
    'D': '&',   'd': '*',
    'E': '(',   'e': ')',
    'F': '-',   'f': '+',
    'G': '=',   'g': '~',
    'H': '{',   'h': '}',
    'I': '[',   'i': ']',
    'J': ':',   'j': ';',
    'K': '<',   'k': '>',
    'L': '?',   'l': '/',
    'M': '1',   'm': '2',
    'N': '3',   'n': '4',
    'O': '5',   'o': '6',
    'P': '7',   'p': '8',
    'Q': '9',   'q': '0',
    'R': '|',   'r': '`',
    'S': '"',   's': "'",
    'T': "A",   't': 'B',
    'U': 'C',   'u': 'D',
    'V': 'E',   'v': 'F',
    'W': 'G',  'w': 'H',
    'X': 'I',  'x': 'J',
    'Y': 'K',  'y': 'L',
    'Z': 'M',  'z': 'N', 
    ' ': 'O',  '.': 'P',
    '?': 'Q',  "'": 'R',
    '!': 'S',  '@': 'T',
    '#': 'U',  '$': 'V',
    '&': 'W',  '(': 'X',
    ')': 'Y',  '-': 'Z',
    '%': 'a',  ',': 'b',
    ':': 'c',  ';': 'd'
}


infile = open('info_security-1.txt', 'r')
outfile = open('encrypted.txt', 'w')

reader = infile.read()
writer = csv.writer(outfile)

for letter in reader:
    if letter in codes:
        outfile.write(codes[letter]) #for a letter in reader find its corresponding code in the dictionary and write that code to the outfile

    
infile.close()
outfile.close()