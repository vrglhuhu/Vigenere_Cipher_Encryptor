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
print("\n\033[33mHi, I am Chean Bernard V. Vergel a first year college student at Polytechnic University of the Philippines.\033[0m")
print("")
name_of_user = input("\033[35mHow about you what is your name?\U0001F917\033[0m ")
print("")
print("\033[36m\U0001F534\U0001F534\U0001F534 This program will encrypt a message using the Vigenère Cipher \U0001F534\U0001F534\U0001F534\033[0m")
print("")

# Ask user for the message and the key.
print("\033[41mFOR MESSAGE\U0001F447\033[0m")
print("")
message = input("\033[32mPlease enter the message:\033[0m ")
message = message.upper().replace(" ", "")
print("")
print("\033[41mFOR KEY\U0001F447\033[0m")
print("")
key = input("\033[32mPlease enter the key:\033[0m ")
key = key.upper().replace(" ", "")
print("")

# Ask the user if want to see the inputted message and key.
agreement = str(input("\033[32mDo you want to see your inputted mesessage and key? \033[0m\033[40m\033[33mYES\033[0m \033[32mor\033[0m \033[40m\033[33mNO:\033[0m "))

# If the user answered yes, print the message and key.
if agreement.upper().replace(" ", "") == "YES":
    print("")
    print("\033[41mYOUR MESSAGE IS:\033[0m " + message)
    print("")
    print("\033[41mYOUR KEY IS:\033[0m " + key)
    print("")

   # Translate the key into corresponding letter values 0 - 25.
    key_map = [ord(i) - 65 for i in key]

   # Encrypt the message.
    ciphertext = ""
    for i in range(len(message)):
        encrypted_num = (ord(message[i]) - 65 + key_map[i % len(key_map)]) % 26
        ciphertext += chr(encrypted_num + 65)

   # Output the ciphertext.
    print("The ciphertext is: " + ciphertext)

   # Create a footer.
    print("")
    print("\033[40m\033[33mThank you for your time\U0001F600\033[0m")
    print("")
    print("")
    goodbye = pyfiglet.figlet_format("Visit me again", font = "digital" )
    print (goodbye)
    print("") 

# Else if the user answered no.
elif agreement.upper().replace(" ", "") == "NO":

   # Translate the key into corresponding letter values 0 - 25.
    key_map = [ord(i) - 65 for i in key]

   # Encrypt the message.
    ciphertext = ""
    for i in range(len(message)):
        encrypted_num = (ord(message[i]) - 65 + key_map[i % len(key_map)]) % 26
        ciphertext += chr(encrypted_num + 65)

   # Output the ciphertext.
    print("\U0001F7E1\U0001F7E1\U0001F7E1\033[32m The ciphertext is: \033[0m" + ciphertext + "\U0001F7E1\U0001F7E1\U0001F7E1")

# Else print invalid key.
    print("")
    print("\033[40m\033[33mInvalid key\U0001F972\033[0m")
    print("")
    quit()

# Create a footer.
    print("\033[40m\033[33mThank you for your time\033[0m")
    print("")
    print("")
    goodbye = pyfiglet.figlet_format("Visit me again", font = "digital" )
    print (goodbye)
    print("")
