import sys

def caesar_cipher(shift):
    message = input().upper()

    #Initialize an empty string to store the encoded message
    encoded_message = ""

    for char in message:
        if char.isalpha():
            #Shift the character by the given amount
            encoded_char = chr((ord(char) - 65 + shift) % 26 + 65)
            #Append the encoded character to the encoded message
            encoded_message += encoded_char
            #Add spaces after every five letters
            if len(encoded_message.replace(" ", "")) % 5 == 0:
                encoded_message += " "

    #Print the encoded message in blocks of five letters, ten blocks per line
    blocks = [encoded_message[i:i+5] for i in range(0, len(encoded_message), 5)]
    for i in range(0, len(blocks), 10):
        print(" ".join(blocks[i:i+10]))

if __name__ == "__main__":
    shift = int(sys.argv[1])
    caesar_cipher(shift)
