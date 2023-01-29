from tkinter import *
import math
PINK = '#FFC0CB'
PEACH = '#FFE5B4'


def reset_timer():
    window.after_cancel(our_timer)


def start_timer():
    count_down(1 * 10)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    # start something action
    if count > 0:
        global our_timer
        our_timer = window.after(1000, count_down, count - 1)


window = Tk()
window.title("Timer")
window.config(padx=100, pady=50, bg=PEACH)

title_label = Label(text="Timer", fg=PINK, font=('Ariel', 50))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=0)
reset_button = Button(text='reset')
reset_button.grid(column=3, row=3)

canvas = Canvas(width=500, height='500')
image = PhotoImage(file='face.png')


timer_text = canvas.create_text(240, 170, text='00:00', )
canvas.grid(column=1, row=1)


window.mainloop()
