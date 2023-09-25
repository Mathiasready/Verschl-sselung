abc=["a","b","c","d","e","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
def encrypt(msg_clear: str, key: int):
    msg_hidden=""
    for c in msg_clear:
        i=abc.index(c)
        new_i=i+key
        new_c=abc[new_i]
        msg_hidden+=new_c
    return msg_hidden

print(encrypt("abc",3))
