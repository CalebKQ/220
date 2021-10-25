# Add your encryption methods here

def encode(mess, key):
    acc = ""
    for c in mess:
        i = ord(c)
        new = chr(i + key)
        acc = acc + new
    return acc

def encode_better(m, n):
    acc = ""
    for i in range(len(m)):
        c = ord(m[i])
        key = ord(n[i % len(n)])
        new = (c + key) - 97
        acc = acc + chr(new)
    return acc