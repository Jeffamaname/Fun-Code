import random

symbols=["+","×","-","÷"]
b=random.randint(1,10)
c=random.randint(1,10)
d=random.randint(0,3)
symbol=symbols[d]
if b<c and symbol=="÷":
    f=b
    b=c
    c=f
print(str(b) + symbol + str(c) + "=?")
a=input()
if symbol=="+":
    if b+c==int(a):
        print("\nRight")
    else:
        print("\nWrong\n" + str(b+c))
elif symbol=="-":
    if b-c==int(a):
        print("\nRight")
    else:
        print("\nWrong\n" + str(b-c))
elif symbol=="×":
    if b*c==int(a):
        print("\nRight")
    else:
        print("\nWrong\n" + str(b*c))
elif symbol=="÷":
    if b//c==int(a):
        print("\nRight")
    else:
        print("\nWrong\n" + str(b//c))