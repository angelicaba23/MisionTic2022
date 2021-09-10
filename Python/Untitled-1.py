x = 3
y=2
x=x%y
x=x%y
y = y %x
print(y)

l = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if l[r][c] % 2 !=0:
            print("*")
#l = 1//5+1//5
#print(l)

l = [x * x for x in range(5)]
#lfor y in range(3)]
def f(lst):
    del lst[lst[2]]
    return lst
print(f(l))

d = {"one":"two","three":"one","two":"three"}
v = d["three"]
for k in range(len(d)):
  v = d[v]
  print(v)
print(v)

x = 1
y=2
x,y,z = x,x,y
z,y,z, = x,y,z
print(x,y,z)

def ff(x):
    if x%2 == 0:
        return 1
    else:return 2
print(ff(ff(2)))
x = float(2)
y = float(4)
print(y**(1/x))

a = 1
b =0
a  = a^b
b  = a^b
a  = a^b

print("a","b","c", sep="sep")