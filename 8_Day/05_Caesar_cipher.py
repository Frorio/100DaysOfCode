alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue == True:

    direction = input("Type 'encode' to enctypt, type 'decode' to dectypt:\n")
    text = input("Type your massage:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else: 
                cipher_text += char
        print(f"The encoded text is {cipher_text}")


    if direction == "encode":
       encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
       encrypt(plain_text=text, shift_amount=-shift) #For decode you just need to shift * -1
    result = input("Do you wanna continue?  Y/N:  ").lower()
    if result == "n": should_continue = False
    else: should_continue = True
print("Have a good time :D")