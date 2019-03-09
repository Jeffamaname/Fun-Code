import random
from tkinter import *

symbols=[]


#functions

def redo():
    if len(str(varr.get()))>3 or score.get(0.0,END)[0]=='0':
        b=random.randint(int(varspn1.get()),int(varspn2.get()))
        c=random.randint(int(varspn1.get()),int(varspn2.get()))
        try:
            symbol=random.choice(symbols)
            if b<c and (symbol=="÷" or symbol=="-"):
                b,c=c,b
            quest=str(b) + " " + symbol + " " + str(c) + " = ?"
            var.set(quest)
            varr.set("")
            textentry.delete(0,END)
        except:
            varr.set("You did't select any operation type")

def click():
    try:
        if len(varr.get())<3 and textentry.get()!="":
            b=str(var.get())
            a=int(textentry.get())
            e=""
            m="the result is "
            n=n1=0
            ri="Right"
            wr="Wrong\n"
            r=score.get(0.0,END)
            r1=score1.get(0.0,END)
            c=b.split(" ")
            if "+" in c:
                if int(c[0])+int(c[2])==a:
                    e=ri
                    n=1
                    if int(r1)==int(r):
                        n1=1
                else:
                    e=wr + m + str(int(c[0])+int(c[2]))
                    n=int(r)*-1
            elif "×" in c:
                if int(c[0])*int(c[2])==a:
                    e=ri
                    n=1
                    if int(r1)==int(r):
                        n1=1
                else:
                    e=wr + m + str(int(c[0])*int(c[2]))
                    n=int(r)*-1
            elif "-" in c:
                if int(c[0])-int(c[2])==a:
                    e=ri
                    n=1
                    if int(r1)==int(r):
                        n1=1
                else:
                    e=wr + m + str(int(c[0])-int(c[2]))
                    n=int(r)*-1
            elif "÷" in c:
                if int(c[0])//int(c[2])==a:
                    e=ri
                    n=1
                    if int(r1)==int(r):
                        n1=1
                else:
                    e=wr + m + str(int(c[0])//int(c[2]))
                    n=int(r)*-1
        varr.set(e)
        score.delete(0.0,END)
        score.insert(END,int(r)+n)
        score1.delete(0.0,END)
        score1.insert(END,int(r1)+n1)
    except:
        textentry.delete(0,END)

def prcd():
    global symbols
    symbols=[]
    if var1.get()==1:
        symbols.append("+")
    if var2.get()==1:
        symbols.append("×")
    if var3.get()==1:
        symbols.append("-")
    if var4.get()==1:
        symbols.append("÷")
    window.grid()
    settings.grid_forget()
    redo()
    
def rtrn():
    window.grid_forget()
    settings.grid()
    score.delete(0.0,END)
    score.insert(END,0)



#root

root=Tk()
root.configure(background="#3b5998")


settings=Frame(root,bg="#3b5998")
settings.grid()

window=Frame(root,bg="#3b5998")



#first frame (settings)

lbl = LabelFrame(settings, text = "Choose Equation Type",bg="#3b5998",fg="#f7f7f7")
lbl.grid()


var1=IntVar()
C1=Checkbutton(lbl,text="Addition (+)",variable=var1,onvalue=1,offvalue=0,height=2,width=20,bg="#3b5998",fg="#f7f7f7",selectcolor="#3b5998",bd=0)

var2=IntVar()
C2=Checkbutton(lbl,text="Multiplication (×)",variable=var2,onvalue=1,offvalue=0,height=2,width=20,bg="#3b5998",fg="#f7f7f7",selectcolor="#3b5998",bd=0)

var3=IntVar()
C3=Checkbutton(lbl,text="Subtraction (-)",variable=var3,onvalue=1,offvalue=0,height=2,width=20,bg="#3b5998",fg="#f7f7f7",selectcolor="#3b5998",bd=0)

var4=IntVar()
C4=Checkbutton(lbl,text="Division (÷)",variable=var4,onvalue=1,offvalue=0,height=2,width=20,bg="#3b5998",fg="#f7f7f7",selectcolor="#3b5998",bd=0)

C1.select()
C2.select()
C3.select()
C4.select()
C1.grid(row=0)
C2.grid(row=1)
C3.grid(row=2)
C4.grid(row=3)

lbl1 = LabelFrame(settings, text = "Number Range",bg="#3b5998",fg="#f7f7f7",width=200)
lbl1.grid()

Label(lbl1,text="from",bg="#3b5998",fg="#f7f7f7").grid(row=0,column=0,sticky='w')
varspn1=StringVar()
spn1=Spinbox(lbl1, from_ = 1, to = 10,width=17,textvariable=varspn1).grid(row=0,column=1,sticky='e')

Label(lbl1,text="to",bg="#3b5998",fg="#f7f7f7").grid(row=1,column=0,sticky='w')
varspn2=StringVar()
spn2=Spinbox(lbl1, from_ = 1, to = 10,width=17,textvariable=varspn2).grid(row=1,column=1,sticky='e')

btn1=Button(settings,text="Proceed",width="3",command=prcd)
btn1.grid(row=5,sticky="E")

btn=Button (settings,text="Exit",width="3",command=quit)
btn.grid(row=5,sticky="W")



#second frame (window)

b1=Button (window,text="Generate Math Problem",width="17",command=redo)
b1.grid(row=0,sticky="N")


var=StringVar()
txt=Label (window,textvariable=var,width="10",height=1,bg="#3b5998",fg="#f7f7f7",font="Arial 17 bold")
txt.grid(row=1,column=0,sticky="N")


Label (window,text="Insert result",bg="#3b5998",fg="#f7f7f7",font="Arial 12").grid(row=2,sticky="N")

textentry=Entry (window,width=20,bg="#3b5998",fg="#f7f7f7")
textentry.grid(row=3,sticky="N")


b2=Button (window,text="Enter",width="3",command=click)
b2.grid(row=4,sticky="N")


score=Text(window,width="3",height="1",bg="#3b5998",fg="#f7f7f7",font="Arial 5 bold")
score.insert(END,0)
score.grid(row=2,column=0,sticky="W")

score1=Text(window,width="3",height="1",bg="#3b5998",fg="#f7f7f7",font="Arial 5 bold")
score1.insert(END,0)
score1.grid(row=2,column=0,sticky="E")


Canvas (window,bg="#3b5998",width="225",height="50").grid()

varr=StringVar()
output=Message(window,textvariable=varr,bg="#3b5998",fg="#f7f7f7",font="Arial 6",anchor="w",width="100")
varr.set(" ")
output.grid(row=5)


Button(window,text="Return",width="3",command=rtrn).grid(row=6,sticky="W")

Button (window,text="Exit",width="3",command=quit).grid(row=6,sticky="E")
root.mainloop()