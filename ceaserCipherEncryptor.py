def caesarCipherEncryptor(string, key):
    string = list(string)
    inRange = False
    while not inRange :
        inRange = True
        if key > 25 :
            key -= 26
        
    for idx in range(len(string)) :
        newASCII = int(ord(string[idx])) + key
        if newASCII > 122 :
            newASCII = 96 + (newASCII - 122)
        string[idx] = chr(newASCII)
        
    return "".join(string)
