import pyttsx3
import PyPDF2
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import *
global r,g,book,pages,pdfreadder
r=150
g=0
master=Tk()
var1 = IntVar()
scale = Scale( master, orient=HORIZONTAL, from_ =250,to =150,variable = var1)
scale.pack(anchor=CENTER)
def setrate():
     global r
     r =var1.get()
b1 = Button(master, text ="Set the rate of words",
            command = setrate,
            bg = "white", 
            fg = "black")
b1.pack()
def gender():
    global g
    g=var2.get()
var2 = IntVar()
r1 = Radiobutton(master, text="Male", variable=var2, value=0,command=gender)
r1.pack( anchor = W )
r2 = Radiobutton(master, text="Female", variable=var2, value=1,command=gender)
r2.pack( anchor = W )
def browse():
    global book,pages,pdfreadder
    book = askopenfilename()
    pdfreadder = PyPDF2.PdfFileReader(book)
    pages = pdfreadder.numPages
b2 = Button(master, text ="Open PDF file",
            command = browse,
            bg = "white", 
            fg = "black")
b2.pack()
def play():
    for num in range(0, pages):
        page = pdfreadder.getPage(num)
        text = page.extractText()
        player = pyttsx3.init()
        rate = player.getProperty('rate')
        player.setProperty('rate', r)
        voices = player.getProperty('voices')
        player.setProperty('voice', voices[g].id)
        player.say(text)
        player.runAndWait()
b3 = Button(master, text ="Play",
            command = play,
            bg = "white", 
            fg = "black",
            width=10)
b3.pack()
label1 = Label( master, text="Select PDF file to be read:")
label2 = Label( master, text="Set the reading speed:")
label3 = Label( master, text="Select voice:")
label1.pack()
label2.pack()
label3.pack()
master.geometry('270x240')
label1.place(x=10,y=10)
b2.place(x=10,y=35)
label2.place(x=10,y=60)
scale.place(x=10,y=80)
b1.place(x=140,y=95)
label3.place(x=10,y=120)
r1.place(x=10,y=140)
r2.place(x=10,y=160)
b3.place(x=100,y=190)
master.mainloop()




