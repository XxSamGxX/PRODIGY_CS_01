alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption():
    try:
        uText=input("Enter the text: ").lower()
        shift_key=int(input("Enter the Shift: "))
        newText=""
        for char in uText:
            if char in alphabet:
                pos= alphabet.index(char)
                newPos= (pos + shift_key)%26
                newText += alphabet[newPos]
            else:
                newText += char
        print("\nText after Encryption: " + newText)
    except:
         print("An Error Occured. Try Again")
def decryption():
    try:
        uText=input("Enter the text: ").lower()
        shift_key=int(input("Enter the Shift: "))
        newText=""
        for char in uText:
            if char in alphabet:
                pos=alphabet.index(char)
                newPos = (pos-shift_key)%26
                newText = newText+alphabet[newPos]
            else:
                newText += char
        print("\nText after Encryption:" + newText)
    except:
        print("An Error Occured. Try again")

End = False
while not End:
    print("Choose from the following:")
    print("1. Encrypt Text \n2. Decrypt Text")
    operation =int(input("What do you want to do: "))
    
    if operation == 1:
        encryption()
    elif operation ==2:
        decryption()
    else:
        print("Choose Between 1 and 2 only")
    con=int(input("Do you want to continue \n1. Yes \n2. No \n"))
    if con == 2:
        End = True
        