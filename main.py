print()
print()
for a in range(1, 2):
    for b in range(1, 21):
        if b % 2 != 0:
            print("~", end=" ")
        else:
            if b == 10:
                print("WELCOME TO CAESAR'S CIPHER", end=" ")
            else:
                print("*", end=" ")
print()
print()

print(
    "Caesar's Cipher is named after Julius Caesar, who used it to protect important military message. You can Encrypt(convert message into Cipher or coded message) using this game.")
print()

key = int(input("Please enter the number that will be used as a key: "))

def read_from_file():
    fp = open("E:\\Puja Das 2023\\Python_files\\PYTHON_PROJECTS\\Caesar's_Cipher.txt", "r")
    word = fp.read()
    return word



def encrypt(plain_text, key):
    step = key
    encrypted_text = ""
    en_char = ""
    for word in plain_text:
        for char in word:
            if char.isalpha():
                if char.isupper():
                    en_char = chr(((ord(char) + step - 65) % 26) + 65)
                elif char.islower():
                    en_char = chr(((ord(char) + step - 97) % 26) + 97)
            elif char.isdigit():
                en_char = char
            elif char.isspace():
                en_char = char
            else:
                en_char = char
            encrypted_text += en_char
    return encrypted_text


def write_to_file(text_encrypt):
    fp = open("E:\\Puja Das 2023\\Python_files\\PYTHON_PROJECTS\\Encrypted_file.txt", "w")
    fp.writelines(text_encrypt)
    print("Bravo! Now, check your encrypted text in the file named Encrypted_file.")


plain_text = read_from_file()
text_encrypt = encrypt(plain_text, key)
write_to_file(text_encrypt)

