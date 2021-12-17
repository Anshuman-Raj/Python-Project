from tkinter import *
from time import strftime, struct_time

# ____________________________________Constants____________________________________________

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = -1
RESET = False
DICT = {0: 4, 1: 1, 2: 2, 3: 3}
# _____________________________________Button Functions___________________________________


def start():
    global reps
    reps += 1

    # For Work time
    if reps % 2 == 0:
        title_canvas.config(text="Work Time", fg=GREEN)
        countdown(WORK_MIN*60)

    # When taking long break after 4 reps of work
    elif (reps+1) % 8 == 0:
        title_canvas.config(text="Long Break", fg=RED)
        countdown(LONG_BREAK_MIN*60)

    # When taking Short breaks
    else:
        title_canvas.config(text="Break Time", fg=PINK)
        countdown(SHORT_BREAK_MIN*60)


def stop():
    global reps
    global RESET
    RESET = True
    reps = -1
    title_canvas.config(text="Start")
    canvas.itemconfig(text_canvas, text="25:00")
    check_label.config(text=tick * reps)
# _____________________________________Countdown__________________________________________


def countdown(count=0):

    global reps
    global RESET
    # Condition for resetting the timer
    if not RESET:
        # Create a struct_time object to display on timer
        minutes = count // 60
        seconds = count % 60
        time_val = struct_time([1, 1, 1, 1, minutes, seconds, 1, 1, 1])

        # Updating timer every second
        canvas.itemconfig(text_canvas, text=strftime("%M:%S", time_val))
        if count > 0:
            window.after(1000, countdown, count-1)
        else:
            check_label.config(text=tick * DICT[((reps // 2 + 1) % 4)])
            start()
    else:
        RESET = False
        return

# _____________________________________UI Setup___________________________________________


window = Tk()
window.title('Pomodoro')
window.configure(padx=100, pady=20, bg=YELLOW)

# For starting the timer
start_button = Button(master=window, command=start, text="Start", justify="right", font=('Arial', 15, 'bold'))
start_button.grid(row=2, column=0)

# For title on the page
title_canvas = Label(master=window, text="Start", justify="center", font=('Courier', 60, "bold"), fg=GREEN, bg=YELLOW)
title_canvas.grid(row=0, column=1)

# For putting tomato and timer
canvas = Canvas(width=530, height=510, bg=YELLOW, highlightthickness=0)
the_tomato = PhotoImage(file='tomato.png')
canvas.create_image(265, 255, image=the_tomato)
text_canvas = canvas.create_text(265, 280, text="25:00", fill='white', font=('Arial', 48, "bold"))
canvas.grid(row=1, column=1)

# For adding reset
stop_button = Button(master=window, command=stop, text="Reset", justify="left", font=('Arial', 15, 'bold'))
stop_button.grid(row=2, column=2)

# For adding Check sign on completion of one rep of work
tick = "✔"
check_label = Label(master=window, text=tick*reps, justify="center", fg='green', bg=YELLOW, font=('Arial', 20, 'bold'))
check_label.grid(row=3, column=1)

window.mainloop()


