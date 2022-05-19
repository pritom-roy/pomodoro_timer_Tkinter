import math
from tkinter import Tk, Canvas, PhotoImage, Label, Button

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
text = ""
timer = None

def reset():
    window.after_cancel(timer)
    global reps, text
    reps = 0
    text = ""
    label2.config(text=text)
    label1.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        stat_countdown()


def stat_countdown():
    global reps
    global text
    reps += 1

    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    work_time = WORK_MIN * 60

    if reps == 2 or reps == 4 or reps == 6:
        count_down(short_break)
        label1.config(text="Break", fg=PINK)
    elif reps == 8:
        count_down(long_break)
        label1.config(text="Break", fg=RED)
    elif reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_time)
        label1.config(text="Work", fg=GREEN)
        text += "✔"
        label2.config(text=text)


window = Tk()
window.title("Pomodoro Countdown")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

label1 = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label1.grid(row=1, column=2)

label2 = Label(text="", font=(FONT_NAME, 14, "bold"), fg=GREEN, bg=YELLOW)
label2.grid(row=4, column=2)

button1 = Button(text="Start", highlightthickness=0, command=stat_countdown)
button1.grid(row=3, column=1)

button2 = Button(text="Reset", highlightthickness=0, command=reset)
button2.grid(row=3, column=4)

window.mainloop()
