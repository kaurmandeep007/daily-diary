s=[10,20,30,40]
for x in s:
    print(x)
s.append(50)
print(s)
b=bytes(s)
type(b)
print(type(b))
c=bytearray(s)
type(c)
print(type(c))
c.append(50)
print(c)
d=list(b)
print(type(d))
d.append(60)
print(d)
for x in d:
    print(x)
d.insert(2,70)
print(d)
d.pop()
print(d)
del d[4]
print(d)
s="howareyou"
s[1:7]
print(s)