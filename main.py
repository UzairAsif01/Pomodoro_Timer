from tkinter import *
import math
from gtts import gTTS
import pygame
import os
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
check_mark = ""
Sessions = 0
timer = NONE
Audio_files = ["Break.mp3", "Long_break.mp3", "Work.mp3"]
pygame.mixer.init()


# ---------------------------- TIMER START/RESET ------------------------------- #


def reset_timer():
    global Sessions
    global check_mark
    window.after_cancel(timer)
    Timer.config(text="Timer")
    canvas.itemconfig(count_down_text, text="00:00")
    Check_mark.config(text="")
    check_mark = ""
    Sessions = 0


def start_timer():
    global Sessions
    Sessions += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if Sessions % 8 == 0:
        Timer.config(text="Break", fg=RED)
        pygame.mixer.music.load(Audio_files[1])
        pygame.mixer.music.play()
        count_down(long_break_sec)
    elif Sessions % 2 == 0:
        Timer.config(text="Break", fg=PINK)
        pygame.mixer.music.load(Audio_files[0])
        pygame.mixer.music.play()
        count_down(short_break_sec)
    else:
        Timer.config(text="Work", fg=GREEN)
        pygame.mixer.music.load(Audio_files[2])
        pygame.mixer.music.play()
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global check_mark
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(count_down_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if Sessions % 8 == 0:
            check_mark += "✔"
            Check_mark.config(text=check_mark)
            check_mark = ""
        elif Sessions % 2 == 0:
            check_mark += "✔"
            Check_mark.config(text=check_mark)
        else:
            Check_mark.config(text="")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("P o m o d o r o")

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
count_down_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

# labels
Timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
Timer.grid(row=0, column=1)
Check_mark = Label(bg=YELLOW, fg=GREEN)
Check_mark.grid(row=3, column=1)

# buttons
start = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset_timer)
start.grid(row=2, column=0)
reset.grid(row=2, column=2)

window.mainloop()
