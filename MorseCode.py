import sys
class morseCode:
    dataset1 = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/ '
}
    dataset2 = {
    'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 
    'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..', 
    'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.', 
    'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._', 
    'Y': '_.__', 'Z': '__..',
    '0': '_____', '1': '.____', '2': '..___', '3': '...__', '4': '...._', 
    '5': '.....', '6': '_....', '7': '__...', '8': '___..', '9': '____.',
    '.': '._._._', ',': '__..__', '?': '..__..', "'": '.____.', '!': '_._.__',
    '/': '_.._.', '(': '_.__.', ')': '_.__._', '&': '._...', ':': '___...',
    ';': '_._._.', '=': '_..._', '+': '._._.', '-': '_...._', '_': '..__._',
    '"': '._.._.', '$': '..._.._', '@': '.__._.', ' ': '/ '
}
    
    turkish_to_english = {
        'Ç': 'C', 'Ğ': 'G', 'İ': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U',
        'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u'
    }

    def preprocess_text(self, text):
        for turkish_char, english_char in self.turkish_to_english.items():
            text = text.replace(turkish_char, english_char)
        
        return text

    def morse_code_decoding(self):
        self.text = input("Enter your morse code to decode: ").strip()
        if self.text == "/kill":
            sys.exit()
        elif self.text.upper() == "C":
            self.start()
        self.text = self.text.split()
        decoded_message = ""
        for index, pattern in enumerate(self.text):
            if pattern == '/':
                pattern = '/ '
            if pattern in self.dataset1.values():
                decoded_message += list(self.dataset1.keys())[list(self.dataset1.values()).index(pattern)]
            elif pattern in self.dataset2.values():
                decoded_message += list(self.dataset2.keys())[list(self.dataset2.values()).index(pattern)]
            else:
                print(f"Something went wrong for the {index + 1}th pattern: {pattern}. \nPlease try again.")
                return self.morse_code_decoding()

        print(decoded_message)
    
        
    def text_encoding(self):
        self.text = input("Enter your text to encode: ").strip()
        if self.text == "/kill":
            sys.exit()
        elif self.text.upper() == "C":
            self.start()
        self.text = self.text.upper()
        self.text = self.preprocess_text(self.text)
        encoded_message = ""
        for i in range(len(self.text)):
            if self.text[i] in self.dataset1:
                encoded_message += self.dataset1[self.text[i]]+" "
            elif self.text[i] in self.dataset2:
                encoded_message += self.dataset2[self.text[i]]+" "
            else:
                print(f"Something went wrong for the {i + 1}th character: {self.text[i]}. \nPlease try again.")
                return self.text_encoding()
        print(encoded_message)
            

    def start(self):
        self.choice = input("Encode a text or decode a morse code? \n(T = encode a text) \n(M = decode a morse code) \n(/kill to stop running the file)").strip()
        if self.choice == "/kill":
            sys.exit()
        elif(self.choice.upper() == 'T'):
            print("You've decided to encode a text. (Q to quit, C to change the choice) ")
            k = ""
            while True:
                k = input("Special command: ").strip()
                if k == "/kill":
                    sys.exit()
                elif k.upper() == "Q":
                    break
                elif k.upper() == "C":
                    self.start()
                else:
                    self.text_encoding()

        elif(self.choice.upper() == "M"):
            print("You've decided to decode a morse code. (Q to quit, C to change the choice) ")
            k = ""
            while True:
                k = input("Special command: ").strip()
                if k == "/kill":
                    sys.exit()
                elif k.upper() == "Q":
                    break
                elif k.upper() == "C":
                    self.start()
                else:
                    self.morse_code_decoding()
        else:
            print("Invalid choice.")
            self.start()