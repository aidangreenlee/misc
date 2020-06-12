#!/usr/bin/env python3
import string
import random
from copy import copy

word = list(input("Enter something to encrypt: ").upper())
d = {}

for i in word:
    if i not in d.values():
        d[i] = [idx for idx,x in enumerate(word) if x == i and x.isalpha()]

crypt = copy(word)
alphabet = list(string.ascii_uppercase)
for i in d.keys():
    if i.isalpha():
        c = random.choice([x for x in alphabet if x != i])
        alphabet.remove(c)
        for j in d[i]:
            crypt[j] = c
print("".join(crypt))
length = max([len(x) for x in d.values()])
hint = random.choice([x for x in d.keys() if len(d[x]) == length])
value = [crypt[x] for x in d[hint]]
print(value[0], "=", hint)
