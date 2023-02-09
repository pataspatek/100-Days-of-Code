from logo import logo
from alphabet import alphabet

def ceasar(text, shift, direction):
    new_msg = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            index = alphabet.index(i) + shift
            new_msg += alphabet[index]
        else:
            new_msg += i
    print(f"The {direction}d messege is: {new_msg}")

print(logo)

chatting = True
while chatting:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
  
    if direction == "encode" or direction == "decode":
        text = input("Type message you want to encode: ").lower()
        shift = int(input("Type the shift number: "))
        ceasar(text, shift, direction)
    else:
        print("Invalid choice.")
        continue

    reset_chatting = True
    while reset_chatting:
        answer = input("\nWould you like to reset encoding machine? 'yes' or 'no' ")

        if answer == "yes":
            reset_chatting = False
        elif answer == "no":
            reset_chatting = False
            chatting = False
            print("Goodbye.")
        else:
            print("Invalid choice.")
            continue