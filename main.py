from tkinter import *
import math

FONT = 'Time new roman'
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# CREATE THE WINDOWS
windows = Tk()
windows.title(string='Pomodoro APP')
windows.config(padx=100, pady=50, background=YELLOW)


# windows.minsize(width=600,height=500)


def start_timer():
    count = 5
    count_down(count * 60)


def count_down(count):
    count_min = math.floor(count / 60)
    print(count_min)
    count_sec = count % 60
    if count > 0:
        windows.after(1000, count_down, count - 1)
    canvas.itemconfig(start_time, text=f"{count_min:02d}:{count_sec:02d}")


# Create the tomato image
canvas = Canvas(width=200, height=223, background=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
start_time = canvas.create_text(102, 135, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Create timer
timer = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

sessions = []


# def start_timer():
#     seconds = 0
#     minutes = 0
#     while minutes < WORK_MIN:
#         seconds += 1
#         if seconds == 60:
#             minutes += 1
#             seconds = 0
#         canvas.itemconfig(start_time, text=f"{minutes:02d}:{seconds:02d}")
#         canvas.update()
#         time.sleep(1)
#         print(seconds)
#     if minutes >= WORK_MIN:
#         sessions.append("✔")
#         check_marks.config(text=f"{' '.join(sessions)}")


def restart_timer():
    global sessions
    sessions = []
    check_marks.config(text=f"{' '.join(sessions)}")


# Create Start button
start = Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)

# Create Restart button
restart = Button(text="Restart", command=restart_timer, highlightthickness=0)
restart.grid(column=2, row=2)

# Create Check marks
check_marks = Label(text=f"{' '.join(sessions)}", foreground=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

windows.mainloop()
