def Keyword (x,y):
    a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    b=[]
    g=[]
    n=0
    e=""
    for i in y:
        b.append(y[y.index(i)])
    for i in b:
        if not i in b[:n]:
            g.append(i)
        n+=1
    à=g + list(filter(lambda i: not i in g, a))
    for i in x:
        e+=a[à.index(i)]
    return "\nYour incrypted message is: " + e

print(Keyword(input("Insert your encrypted message: "),input("\nInsert keyword: ")))