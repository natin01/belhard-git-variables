s1=input()
s2=input()
print(f"Вы ввели строку {s1} и {s2}")
print(f"Их длина соответственно {len(s1)} и {len(s2)}")
print(f"Первый символ первой строки:{s1[0]}")
print(f"Последний символ последней строки:{s2[-1]}")
print(s1==s2)
print(s1 in s2)
print("А наоборот?", s2 in s1)

a=input("а:")
b=input("b:")
c=input("c:")
nn=int(a)**2+int(b)**2
print(nn)
dn=int(b)*3-4
print(dn)
res1=nn/dn
print(res1)
res2=int(c)**5*4/6
print(res2)
print(res1//res2)
print(res1%res2)

