from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✅"
REPS = 1
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    banner.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    cycle_count.config(text="")
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN

    break_time = "Break"
    work_time = "Work"

    if REPS == 8:
        countdown(LONG_BREAK_MIN * 60)
        banner.config(text=break_time, fg=RED)
        reset_timer()
    elif REPS % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        banner.config(text=break_time, fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        banner.config(text=work_time, fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global REPS, TICK, TIMER

    ticks_shown = ""

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
        TIMER = window.after(1000, countdown, count - 1)
    else:
        REPS += 1
        start_timer()
        work_sessions = math.floor(REPS / 2)
        for n in range(work_sessions):
            ticks_shown += TICK
        cycle_count.config(text=ticks_shown)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

banner = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
banner.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

cycle_count = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18, "bold"))
cycle_count.grid(column=1, row=3)


window.mainloop()
