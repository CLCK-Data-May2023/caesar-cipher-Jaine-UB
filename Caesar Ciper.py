encryption = {
    "a" : "f",
    "b" : "g",
    "c" : "h",
    "d" : "i",
    "e" : "j",
    "f" : "k",
    "g" : "l",
    "h" : "m",
    "i" : "n",
    "j" : "o",
    "k" : "p",
    "l" : "q",
    "m" : "r",
    "n" : "s",
    "o" : "t",
    "p" : "u",
    "q" : "v",
    "r" : "w",
    "s" : "x",
    "t" : "y",
    "u" : "z",
    "v" : "a",
    "w" : "b",
    "x" : "c",
    "y" : "d",
    "z" : "e"
    }



normal_sentence = input("Please enter a sentence: ").lower()

encrypted_sentence = ''

for letter in normal_sentence:
    if letter in encryption:
        encrypted_sentence += encryption[letter]
    else:
        encrypted_sentence += letter

print("Encrypted sentence is:", encrypted_sentence)
        
        
