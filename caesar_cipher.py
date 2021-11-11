#This program takes in input from user and encodes the message using a Caesar Cipher.

from enum import IntEnum

class Action(IntEnum):
    Encrypt = 0
    Decrypt = 1

def get_user_choice():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str=",".join(choices)
    selection=int(input(f"Enter a choice to either encrypt or decrypt a caeser cipher message ({choices_str}): "))
    action=Action(selection)
    return action
    

def caesar_cipher(message,encryption_key):
    result = ""
   # transverse the plain text
    for i in range(len(message)):
       char = message[i]
       if (char.isupper()):
           result += chr((ord(char) + int(encryption_key)-65) % 26 + 65)
       else:
           result += chr((ord(char) + int(encryption_key) - 97) % 26 + 97)
    return result

#check the above function

while True:
    try:
        user_choice = get_user_choice()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue
    
    if user_choice==Action.Encrypt:
        print("Enter a message to encrypt.")
        message= input()
        print("Enter a shift key.")
        encryption_key=input()
        print ("Plain message : " + message)
        print ("Shift pattern : " + encryption_key)
        encrypted_message=caesar_cipher(message,encryption_key)
        print( "Cipher: " + encrypted_message)

    else:
        print("Decrypt a caesar cipher message by entering the encrypted message and the shift key")
        print("Enter a encrypted message: ")
        inputed_encrypted_message=input()
        print("Enter the Caesar Cipher shift key: ")
        inputed_encryption_key=input()
        decrypted_message=caesar_cipher(inputed_encrypted_message, (26-(int(inputed_encryption_key))))
        print(decrypted_message)

    keep_going=input("Do yo want to encrypt or decrpty another message? (y/n): ")
    if keep_going.lower() !="y":
        break
