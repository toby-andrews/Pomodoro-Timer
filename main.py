from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_clicked():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    heading.config(text="Timer")
    check.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_clicked():
    global REPS
    REPS += 1
    if REPS % 2 != 0:
        countdown(WORK_MIN * 15)
        heading.config(text="Work", bg=YELLOW, fg=GREEN, font=("Arial", 45, "bold"))
    elif REPS % 2 == 0 and REPS != 8:
        countdown(SHORT_BREAK_MIN * 15)
        heading.config(text="Short Break", bg=YELLOW, fg=PINK, font=("Arial", 45, "bold"))

    else:
        countdown(LONG_BREAK_MIN * 60)
        heading.config(text="Long Break", bg=YELLOW, fg=RED, font=("Arial", 45, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    global REPS
    count_min = math.floor(count / 60)
    count_sec = round(count % 60, 2)
    if count_sec == 0:
        count_sec = "00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_clicked()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50)
window.configure(bg=YELLOW)

# Canvas
canvas = Canvas(width=210, height=224)
canvas.configure(bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, fill="white", text='25:00', font=("Arial", 35, "bold"))
canvas.grid(column=1, row=1)

# Heading
heading = Label(text="Timer", bg=YELLOW, fg=GREEN, font=("Arial", 45, "bold"))
heading.grid(column=1, row=0)

# Start button
start = Button(text="Start", highlightthickness=0, command=start_clicked)
start.grid(column=0, row=2)

# Stop button
reset = Button(text="Reset", highlightthickness=0, command=reset_clicked)
reset.grid(column=2, row=2)

# Check marks
check = Label(bg=YELLOW, fg=GREEN, font=("Arial", 25, "bold"))
check.grid(column=1, row=3)

window.mainloop()
