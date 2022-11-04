import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            end_text += alphabet[new_position]
        else: 
            end_text += char      
    print(f"The {direction}d text is {end_text}") 



restart = True
while restart:
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    user_shift = int(input("Type the secret number:\n"))
    # Allows for any number to be used as shift
    shift = user_shift % 26

    caesar(text, shift, direction)

    restart_prompt = input("Would you like to use Caesar Cipher again? Type 'yes' or 'no'.\n")
    if restart_prompt == "no":
        restart = False
        print("Goodbye!")




# Non Refactored Version:
"""
def encrypt(text, shift):
    cipher = ""
    for letter in text: 
        letter_index = int(alphabet.index(letter) + shift)   
        new_letter = alphabet[letter_index]
        cipher += new_letter
    print(f"The encoded text is {cipher}")   
    
def decrypt(text, shift):
    plain_text = ""
    for letter in text: 
        letter_index = int(alphabet.index(letter) - shift)   
        new_letter = alphabet[letter_index]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}") 

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
"""
  

    