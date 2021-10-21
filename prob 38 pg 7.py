S=str(input("Dati un sir: "))
#a
a=S.count("A")
print("a) Numarul de aparitii a caracterului 'A': ",a)
#b
if "A" in S:
    for i in S:
        b=S.replace("A","*")
    print("b) Sirul obtinut in urma substituirii: ",b)
else:
    print("b) ",S)
#c
if "B" in S:
    for i in S:
        c=S.replace("B","")
    print("c) Sirul obtinut prin radierea a tuturor aparitiilor caracterului 'B': ",c)
else:
    print("c) ",S)
#d
if "MA" in S:
    for i in S:
        d=S.count("MA")
    print("d) Numarul de aparitii a silbei 'MA': ",d)
else:
    print("d) Nu avem silaba 'MA' in sirul dat")
#e
if "MA" in S:
    for i in S:
        e=S.replace("MA","TA")
    print("e) Substituirea silabei 'MA' cu 'TA': ",e)
else:
    print("e) Nu avem silaba 'MA' in sirul dat")
#f
if "TO" in S:
    for i in S:
        f=S.replace("TO","")
    print("f) Sirul obtinut prin radierea a tuturor aparitiilor silabe 'TO': ",f)
else:
    print("f) ",S)
#g
s=len(S)
g=S[s::-1]
print("g) Sirul invers: ",g)
