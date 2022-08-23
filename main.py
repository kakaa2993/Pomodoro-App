from tkinter import *
import math

FONT = 'Time new roman'
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# CREATE THE WINDOWS
windows = Tk()
windows.title(string='Pomodoro APP')
windows.config(padx=100, pady=50, background=YELLOW)

# 25 , sort break ,25 , short break,25 , short break,25 , long break
# short break 1, 3, 5
# work 0,2,4,6
# long break 7


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        title_label.config(text="Work", fg=RED)
        count_down(work_sec)
    elif reps % 2 == 1:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    elif reps % 7 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=GREEN)
    print(reps)
    reps += 1


def count_down(count):
    global reps, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count > 0:
        timer = windows.after(1000, count_down, count - 1)
    canvas.itemconfig(start_time, text=f"{count_min:02d}:{count_sec:02d}")
    if count == 0 and reps != 7:
        start_timer()
        if reps % 2 == 0:
            sessions.append("✔")
            check_marks.config(text=f"{' '.join(sessions)}")


def restart_timer():
    global sessions, reps, timer
    sessions = []
    reps = 0
    check_marks.config(text=f"{' '.join(sessions)}")
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(start_time, text="00:00")
    windows.after_cancel(timer)


# Create the tomato image
canvas = Canvas(width=200, height=223, background=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
start_time = canvas.create_text(102, 135, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Create timer
title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

sessions = []


# Create Start button
start = Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)

# Create Restart button
restart = Button(text="Restart", command=restart_timer, highlightthickness=0)
restart.grid(column=2, row=2)

# Create Check marks
check_marks = Label(foreground=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

windows.mainloop()
