import Caesar
print("Willkommen zum Verschlüsselungsverfahren")
print("-"*60)
while True:
    msg_clear=input("Was willst du verschlüsseln? (Space um zum beednden)")
    if msg_clear =="":
        break
    key=int(input("Welches Passwort möchtest du verwenden?"))
    msg_hidden=Caesar.encrypt(msg_clear, key)
    print(msg_hidden)
