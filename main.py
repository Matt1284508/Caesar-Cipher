alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the secret number:\n"))

def caesar(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        end_text += alphabet[new_position]
    print(f"The {direction}d text is {end_text}") 
    
caesar(text, shift, direction)

#def encrypt(text, shift):
#    cipher = ""
#    for letter in text: 
#        letter_index = int(alphabet.index(letter) + shift)   
#        new_letter = alphabet[letter_index]
#        cipher += new_letter
#    print(f"The encoded text is {cipher}")   
#    
#def decrypt(text, shift):
#    plain_text = ""
#    for letter in text: 
#        letter_index = int(alphabet.index(letter) - shift)   
#        new_letter = alphabet[letter_index]
#        plain_text += new_letter
#    print(f"The decoded text is {plain_text}") 

#if direction == "encode":
#    encrypt(text, shift)
#elif direction == "decode":
#    decrypt(text, shift)
  



    