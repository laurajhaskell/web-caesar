from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted_text = ""
    for pos in range(len(text)):
        encrypted_text += rotate_character(text[pos],int(rot))
    return encrypted_text   


def main():
    #from sys import argv
    message = input("Type a message:")
    rotation = input("Rotate by:")
    print(encrypt(message, rotation))

if __name__ == "__main__":
    main()