from tkinter import *

#start
window = Tk()
# title of window
window.title('Book scraper')
# set starting size of window
window.minsize(width=500, height=500)
# we can have label
label1 = Label(text='Test', font=("Arial", 24, "bold"))
# place button where you want (two options - pack and place)
label1.pack(side="bottom")
# label1.place(x=50, y=0)

# two ways to config properties of label
label1['text'] = 'BOOK'      # first way
label1.config(text='Book1')  # second way

def press_button():
    print("Button pressed")
# everything we take something with get we get "str"
    new_text = entry1.get()  # need to have entry to can change text with button
    label1.config(text=new_text)

# create button
button = Button(text='GET BOOK', command=press_button)
button.pack()

# create entry
entry1 = Entry(width=50)
entry1.pack()



window.mainloop()
#end