from tkinter import *

fenetre=Tk()
fenetre.title("Trace fonction")
fenetre.geometry("420x400")

label_fonction=Label(fenetre,text="f(x) : ")
label_fonction.place(x=30,y=30)

entry_fonction=Entry(fenetre,bg="white")
entry_fonction.place(x=60,y=30,width=100)

frame1=Frame(fenetre)
frame1.place(x=200)

label_xmin=Label(frame1,text="xmin : ")
label_xmin.grid(row=1,column=1)

label_xmax=Label(frame1,text="xmax : ")
label_xmax.grid(row=2,column=1)

label_ymin=Label(frame1,text="ymin : ")
label_ymin.grid(row=1,column=3)

label_ymax=Label(frame1,text="ymax : ")
label_ymax.grid(row=2,column=3)

entry_xmin=Entry(frame1,bg="white",width=10)
entry_xmin.insert(0, "-5")
entry_xmin.grid(row=1,column=2)

entry_xmax=Entry(frame1,bg="white",width=10)
entry_xmax.insert(0, "5")
entry_xmax.grid(row=2,column=2)

entry_ymin=Entry(frame1,bg="white",width=10)
entry_ymin.insert(0, "-5")
entry_ymin.grid(row=1,column=4)

entry_ymax=Entry(frame1,bg="white",width=10)
entry_ymax.insert(0, "5")
entry_ymax.grid(row=2,column=4)

H = 300
W = 380
canvas=Canvas(fenetre,background="white")
canvas.place(y=80,width=W,height=H,x=20)

def tracer():
    xmin = int(entry_xmin.get())
    xmax = int(entry_xmax.get())
    ymin = int(entry_ymin.get())
    ymax = int(entry_ymax.get())
    canvas.create_rectangle(0, 0, W, H, fill="white")
    canvas.create_line(10,10,100,300)

button_tracer=Button(fenetre,text="Tracer",command=tracer)
button_tracer.place(x=180,y=50)

fenetre.mainloop()