# Vergel, Chean Bernard Villanueva
# Assignment No. 3
# Question No. 3

# This program will encrypt a message using the Vigenère Cipher.
# Create a header.
import pyfiglet
print("")
print("")
print("=" * 70)
print("=" * 70)
print("")
welcome_one = pyfiglet.figlet_format("My Vigenère ".center(5, " "), font = "puffy" )
print(welcome_one) 
welcome_two = pyfiglet.figlet_format("Cipher".center(13, " "), font = "puffy" )
print(welcome_two) 
print("=" * 70)
print("=" * 70)
# Ask for the name of the user.
print("Hi, I am Chean Bernard V. Vergel a first year college student at Polytechnic University of the Philippines.")
print("")
name_of_user = input("How about you what is your name? ")
print("")
print("This program will encrypt a message using the Vigenère Cipher ")
print("")
# Ask user for the message and the key.
print("FOR MESSAGE")
print("")
message = input("Please enter the message: ")
message = message.upper().replace(" ", "")
print("")
print("FOR KEY")
print("")
key = input("Please enter the key: ")
key = key.upper().replace(" ", "")
print("")
# Ask the user if want to see the inputted message and key.
agreement = str(input("Do you want to see your inputted mesessage and key? YES or NO: "))
# If the user answered yes, print the message and key.
if agreement.upper().replace(" ", "") == "YES":
    print("")
    print("YOUR MESSAGE IS: " + message)
    print("")
    print("YOUR KEY IS: " + key)
    print("")
   # Translate the key into corresponding letter values 0 - 25.
    key_map = [ord(i) - 65 for i in key]
   # Encrypt the message.
    for i in range(len(message)):
        encrypted_num = (ord(message[i]) - 65 + key_map[i % len(key_map)]) % 26
        ciphertext += chr(encrypted_num + 65)
   # Output the ciphertext.
# Else if the user answered no.
   # Translate the key into corresponding letter values 0 - 25.
   # Encrypt the message.
   # Output the ciphertext.
# Else print invalid key.
# Create a footer.
