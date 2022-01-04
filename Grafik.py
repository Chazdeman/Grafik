from tkinter import *
klik=0
def clikerrr(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
    if klik==100:
       klik=0

def clikerrr_minus(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
    if klik==-100:
       klik=0 

def txt_to_lbl(event):
    #pass
    text=txt.get()#from Entry to text
    lbl.configure(text=text)
    txt.delete(0,END)

def vibor():
    viber=var.get()
    lbl.configure(text=viber)
    txt.insert(0,viber)
    txt.delete(0,END)

aken=Tk()
aken.title("Nikita")
aken.geometry("1920x1080")
nupp=Button(aken,text="Тыкни меня",font="Times_New_Roman 20", fg="blue", bg="black", height=4, width=20 , relief=GROOVE )
nupp.bind("<Button-1>",clikerrr)#LKM
nupp.bind("<Button-3>",clikerrr_minus)#PKM
lbl=Label(aken,text="Здесь был я!", height=4, width=20, font="Arial 20", fg="black", bg="pink")
txt=Entry(aken,font="Times_New_Roman 30", fg="red", bg="black",justify=RIGHT)
txt.bind("<Return>",txt_to_lbl)#Enter
i1=PhotoImage(file="jabloko (2).gif")
i3=PhotoImage(file="tort.gif")
i2=PhotoImage(file="totem.gif")
var=StringVar()
var.set("ODIN")
r1=Radiobutton(aken,image=i1,variable=var,value="ODIN",command=vibor)
r3=Radiobutton(aken,image=i2,variable=var,value="DVA",command=vibor)
r2=Radiobutton(aken,image=i3,variable=var,value="THRI",command=vibor)

lbl.pack()
nupp.pack(side=TOP)#side = LEFT, TOP, RIGHT
txt.pack()
r1.pack(side=LEFT)
r2.pack(side=RIGHT)
r3.pack(side=TOP)
aken.mainloop()