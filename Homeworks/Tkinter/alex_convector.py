from tkinter import *

def euro_to_leva():
    euro = float(euro_input.get())
    leva = euro * 1.95
    leva_result.config(text=leva)

window1 = Tk()
window1.title("Euro to leva")

euro_input = Entry(width=7)
euro_input.grid(column=1, row=0)

euro_label = Label(text="Euro")
euro_label.grid(column=2, row=0)

leva = Label(text="Result: ")
leva.grid(column=0, row=1)

leva_result = Label(text='0')
leva_result.grid(column=1, row=1)

leva_lable = Label(text="Lv")
leva_lable.grid(column=2, row=1)

convert_button = Button(text="Convert", command=euro_to_leva)
convert_button.grid(column=1, row=2)
window1.mainloop()