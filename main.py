from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#4cb870"
YELLOW = "#f7f5dd"
FONT_NAME = "Comfortaa"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def create_button(column, row, text, button_command):
    """Place buttons on the canvas"""
    button = Button(text=text, font=(FONT_NAME, 13, "bold"), bg=YELLOW, activebackground=YELLOW,
                    fg=GREEN, activeforeground=GREEN)
    button.config(padx=20, pady=10, command=button_command)
    button.grid(column=column, row=row)
    return button


def create_checkmark(checks):
    """Place checks on the canvas"""
    checkmark_label = Label(text=checks, font=(FONT_NAME, 24), fg=GREEN, bg=YELLOW)
    checkmark_label.config(padx=10, pady=40)
    checkmark_label.grid(column=1, row=2)


def reset():
    """Reset the timer (when the btn is pressed)"""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Pomodoro")
    create_checkmark(" ")
    global reps
    reps = 0


def start_timer():
    """Define the timer mechanism (break length and time label colors)"""
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)


def countdown(count):
    """Display time left and how many reps the user did already"""
    timer_min = math.floor(count / 60)
    timer_sec = count % 60
    if timer_sec < 10:
        timer_sec = f"0{timer_sec}"
    if timer_min < 10:
        timer_min = f"0{timer_min}"
    timer_time = f"{timer_min}:{timer_sec}"

    canvas.itemconfig(timer_text, text=timer_time)
    if count >= 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps == 2:
            create_checkmark("✓")
        elif reps == 4:
            create_checkmark("✓ ✓")
        elif reps == 6:
            create_checkmark("✓ ✓ ✓")
        elif reps == 8:
            create_checkmark("✓ ✓ ✓ ✓")


###### TKINTER UI SETUP ######

window = Tk()
window.title("Pomodoro Timer")
window.iconbitmap("tomato_icon.ico")
window.config(padx=50, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=222, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(111, 112, image=tomato_img)
timer_text = canvas.create_text(111, 132, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_button = create_button(column=0, row=2, text="START", button_command=start_timer)
reset_button = create_button(column=2, row=2, text="RESET", button_command=reset)

# Labels
create_checkmark(" ")
title_label = Label(text="Pomodoro", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, width=8)
title_label.config(padx=10, pady=40)
title_label.grid(column=1, row=0)

window.mainloop()
