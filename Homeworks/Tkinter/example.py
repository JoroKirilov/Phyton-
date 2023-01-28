from tkinter import *

# https://www.tcl.tk/man/tcl8.6.13/TkCmd/entry.html

# start
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
# label1.grid(columnspan=3, rowspan=3, row=1, column=2)

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


def check_on_off():              # that returns 0 or 1 when click on check button
    print(check_state.get())


# create check button
check_state = IntVar()
check_button1 = Checkbutton(text='Turn ON/OFF', variable=check_state, command=check_on_off)
check_state.get()
check_button1.pack()

def radio_used():
    print(radio_state.get())
# create radio button
radio_state = IntVar()
radio_button1 = Radiobutton(text='Opt1', value=1, variable=radio_state, command=radio_used)
radio_button2 = Radiobutton(text='Opt2', value=2, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()

def use_listbox(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=3)
options1 = ['author', 'pages', 'title']
for option in options1:
    listbox.insert(options1.index(option), option)

listbox.bind("<<ListBoxSelect>>", use_listbox)
listbox.pack()
window.mainloop()
#end



# за бутона има state - NORMAL, DISABLED.
# може във функцията press_button да сложим button['state'] =
# DISABLED и така става неактивен