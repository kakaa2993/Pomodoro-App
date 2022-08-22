from tkinter import *
import time

FONT = 'Time new roman'
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# CREATE THE WINDOWS
windows = Tk()
windows.title(string='Pomodoro APP')
windows.config(padx=100, pady=50, background=YELLOW)
# windows.minsize(width=600,height=500)

# Create the tomato image
canvas = Canvas(width=200, height=223, background=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
start_time = canvas.create_text(102, 135, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
# canvas.create_text(100, 200,text="Timer", font=(FONT_NAME,50 ,"bold"), fill=GREEN)
canvas.grid(column=1, row=1)

# Create timer
timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)


def start_count():
    seconds = 0
    minutes = 0
    while minutes < 25:
        seconds += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
        canvas.itemconfig(start_time, text=f"{minutes:02d}:{seconds:02d}")
        canvas.update()
        time.sleep(1)
        print(seconds)


# Create Start button
start = Button(text="Start", command=start_count)
start.grid(column=0, row=2)

windows.mainloop()
