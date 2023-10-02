abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
       "v", "w", "x", "y", "z"]


def encrypt(msg_clear: str, key: int):
    msg_hidden = ""
    for c in msg_clear.lower():
        try:
            i = abc.index(c)
            new_i = (i + key) % 26
            new_c = abc[new_i]
        except ValueError:
            if c.isnumeric():
                i = int(c)
                new_i = (i + key) % 10
                new_c = str(new_i)
            else:
                new_c = c
        msg_hidden += new_c
    return msg_hidden


def decrypt(hidden_msg: str, key: int):
    return encrypt(hidden_msg, -key)
