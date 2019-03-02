def Caesar (x,y):
    a="abcdefghijklmnopqrstuvwxyz"
    b=c=d=""
    if y in range (1,26):
        for i in x:
            try:
                b+=a [y-len (a [a.index (i):])]
            except (ValueError):
                if i in a.upper () :
                    b+=a.upper () [y-len (a.upper () [a.upper ().index (i):])]
                elif i==" ":
                    b+=i
                else:
                    c+=" " + i
                    d="\nCharacter(s)%s unsupported (only alphabet and punctuation)" % c
    else:
        return "\nShift count %s out of range (only 1 to 25)" % y
    if d=="":
        return "\nYour incrypted message is: " + b
    else:
        return d
message=str (input ("Insert your message: "))
try:
    shift=int (input ("\nInsert character shift (optional): "))
except (ValueError):
    shift=1
print (Caesar (message,shift))
