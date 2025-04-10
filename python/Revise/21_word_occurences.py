s = "I work in Onebill after my bachelor's degree I"

tokens = s.split(" ")
print(tokens)
d = {}
for token in tokens:
    if token in d:
        d[token] += 1
    else:
        d[token] = 1

print(d)