import string
import random

s1 = string.ascii_letters
s2 = string.ascii_uppercase
s3 = string.ascii_lowercase
s4 = string.punctuation
try:
    plen = int(input("enter the pasword length\n"))
    s = []

    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    print("Your password is:","".join(s[0:plen]))
except:
    pass