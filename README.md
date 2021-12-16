caesar cipher.py program takes as input a message and a shift key then using the caser cipehr ecrypts the message. There is also an 
option to input a encrypted message and the shift key to decrypt a message.

First the IntEnum module is imported at the start of the proram. This defines symbolic names bound to unique constant values so that
there is no issue with user input. All they have to do is type a number which correposnds to the choice. In this case 0 for encrypting
and 1 for decrptying a caser cipher.

The first function get_user_choice was defined to asertain if the user wasnts to either encrypt or decrypt a message.

The next function is the casesar_cipher fucntion which takes the message and the encryption key. A loop goes through 
each character of the message and using Ascii code and the key that original character is shifted to create the encryption.
This same function is also used to decrypt. The encrypted message is inputed and when the user inputs the key
it is subtracted from 26 which creates a decryption key.

The body of the function is a while loop that continues to ask the user if they either want to encrypt or decrypt a message. 
