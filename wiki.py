from tkinter import *
import wikipedia
from tkinter.font import Font

root = Tk()
root.geometry('1320x670+15+15')
my_font= Font(family='Times New Roman',size=36,weight='bold')
my_font2 = Font(family="Calibri",size=12)
my_font3 = Font(family='Calibri',size=16)
def search_it():
    try:
        key = entry_text.get()
        wiki = wikipedia.summary(key)
        text.delete(1.0,END)
        text.insert(INSERT,wiki)
    except:
        text.delete(1.0, END)
        text.insert(INSERT, "You're Giving Wrong Input OR Check Your Internet Connection.")

top_frame = Frame(root)
label = Label(top_frame,text='Wikipedia',font=my_font)
label.pack()
entry_text = StringVar()
entry = Entry(top_frame,text=entry_text,width=40,font=my_font2)
entry_text.set('Please Write Here Something To Search...')
entry.pack(side=LEFT)
bt1 = Button(top_frame,text='Search',command=search_it)
bt1.pack()
top_frame.pack()

bottom_frame = Frame(root)
scroll = Scrollbar(bottom_frame)
text = Text(bottom_frame,height=20,yscrollcommand=scroll.set,wrap=WORD,font=my_font3)
scroll.config(command=text.yview)
scroll.pack(fill=Y,side=RIGHT)
text.pack()
frame3 = Frame(root)
label2 = Label(frame3,text='(Made With Love By Sunny Arora)')
label2.pack()
bottom_frame.pack()
frame3.pack(side=TOP)
root.mainloop()