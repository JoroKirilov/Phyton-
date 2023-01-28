from tkinter import *

window1 = Tk()
window1.title('currency converter')
window1.minsize(width=500, height=500)


label1 = Label(text='Currency converter', font=("Arial", 24, "bold"))
label1.pack()

label_text = Label(text='Enter lv :', font=("Arial", 10, "bold"))
label_text.pack()
label_text.place(x=5, y=50)

label_text1 = Label(text=0)
label_text1.pack()

entry1 = Entry(width=50)
entry1.focus()
entry1.pack()
entry1.place(x=10, y=80)

def convert_currency():
    result = int(entry1.get())
    result = result * 1.95
    label_text1.config(text=result)


button1 = Button(text='Convert', command=convert_currency)
button1.pack()
button1.place(x=40, y=100)


window1.mainloop()