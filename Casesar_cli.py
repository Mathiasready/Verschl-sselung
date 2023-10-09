import Caesar

print("Willkommen zum Verschlüsselungsverfahren")
print("-" * 60)


def do_encrypt():
    msg_clear = input("Was willst du verschlüsseln?")
    key = get_key()
    msg_hidden = Caesar.encrypt(msg_clear, key)
    print(msg_hidden)


def do_decrypt():
    msg_clear = input("Was willst du entschlüsseln?")
    d_key = get_key()
    msg_hidden = Caesar.decrypt(msg_clear, d_key)
    print(msg_hidden)


def get_key():
    while True:
        try:
            d_key = int(input("Welches Passwort möchtest du verwenden?"))
            break
        except ValueError:
            print("Bitte eine ganze Zahl eingeben")
    return d_key


def do_bruteforce():
    msg_clear = input("Was willst du entschlüsseln?")
    for key in range(26):
        msg_hidden = Caesar.decrypt(msg_clear, key)
        print(f"{key:02d}: {msg_hidden}")


while True:
    selection = input("was möchtest du tun? (e)ncrypt, (d)ecrypt, (b)rute, force e(x)it")
    if selection == "e":
        do_encrypt()
    elif selection == "d":
        do_decrypt()
    elif selection == "b":
        do_bruteforce()
    elif selection == "x":
        break
    else:
        print(f"Funktion {selection} konnte nicht gefunden werden")
