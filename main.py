MORSE_CODE_DICT = {'A': '.-',
                   'B': '-...',
                   'C': '-.-.',
                   'D': '-..',
                   'E': '.',
                   'F': '..-.',
                   'G': '--.',
                   'H': '....',
                   'I': '..',
                   'J': '.---',
                   'K': '-.-',
                   'L': '.-..',
                   'M': '--',
                   'N': '-.',
                   'O': '---',
                   'P': '.--.',
                   'Q': '--.-',
                   'R': '.-.',
                   'S': '...',
                   'T': '-',
                   'U': '..-',
                   'V': '...-',
                   'W': '.--',
                   'X': '-..-',
                   'Y': '-.--',
                   'Z': '--..',
                   '1': '.----',
                   '2': '..---',
                   '3': '...--',
                   '4': '....-',
                   '5': '.....',
                   '6': '-....',
                   '7': '--...',
                   '8': '---..',
                   '9': '----.',
                   '0': '-----',
                   ', ': '--..--',
                   '.': '.-.-.-',
                   '?': '..--..',
                   '/': '-..-.',
                   '-': '-....-',
                   '(': '-.--.',
                   ')': '-.--.-',
                   " ": " "
                   }

end = False
while not end:
    text_to_code = input("Hello,enter text you want to translate to morse code.For end the program type END").upper()
    if text_to_code == "END":
        break
    end_text = ""
    new_letter = ""
    for letter in text_to_code:
        if MORSE_CODE_DICT.get(letter):
            end_text += MORSE_CODE_DICT.get(letter)

    print(end_text)













