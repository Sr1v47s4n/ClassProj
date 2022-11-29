import secrets
import string


def hashgen():
    small = string.ascii_lowercase
    num = string.digits
    caps = string.ascii_uppercase

    mix = small + num + caps

    hash_length = 28

    hash = ""
    for i in range(hash_length):
        hash += "".join(secrets.choice(mix))
    return hash
