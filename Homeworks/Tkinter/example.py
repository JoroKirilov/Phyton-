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
entry1.insert(END, string='Change name of label1:')

# create text BOX ( WHERE CAN WE ENTER TEXT
text1 = Text()
# focus is where cursor is when start program ( can be in only one place)
text1.focus()
text1.pack()
text1.insert(END, "example text")  # INSERT DEFAULT TEXT
print(text1.get("1.0", END))    # TRY TO GET TEXT

def spinbox_get():
    print(spinbox1.get())

# create spinbox
spinbox1 = Spinbox(from_=0, to=20, width=5, command=spinbox_get)
spinbox1.pack()


def scale_get(value):
    print(value)

# create scale
scale1 = Scale(from_=0, to=100, command=scale_get)
scale1.pack()


window.mainloop()
#end