from tkinter import *
from tkinter import ttk
import math
from datetime import datetime
import json
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Toggle for testing
TEST_MODE = True
WORK_MIN = 1 if TEST_MODE else 25
SHORT_BREAK_MIN = 1 if TEST_MODE else 5
LONG_BREAK_MIN = 2 if TEST_MODE else 20

SETTINGS_FILE = "pomodoro_settings.json"
STATS_FILE = "pomodoro_stats.json"

completed_sessions = []
current_session_start = None

reps = 0
timer = None
is_timer_running = False
is_paused = False
remaining_time = 0

# ---------------------------- SETTINGS MANAGEMENT ------------------------------- #
def load_settings():
    """Load user preferences from settings file."""
    global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, 'r') as file:
                settings = json.load(file)
                WORK_MIN = max(1, settings.get("work_min", WORK_MIN))
                SHORT_BREAK_MIN = max(1, settings.get("short_break_min", SHORT_BREAK_MIN))
                LONG_BREAK_MIN = max(1, settings.get("long_break_min", LONG_BREAK_MIN))
        except json.JSONDecodeError:
            status_bar.config(text="Error loading settings. Resetting to defaults.")

def save_settings():
    """Save current timer settings."""
    settings = {
        "work_min": WORK_MIN,
        "short_break_min": SHORT_BREAK_MIN,
        "long_break_min": LONG_BREAK_MIN,
    }
    try:
        with open(SETTINGS_FILE, 'w') as file:
            json.dump(settings, file)
            status_bar.config(text="Settings saved successfully!")
    except IOError:
        status_bar.config(text="Error saving settings!")

# ---------------------------- TIMER CONTROL ------------------------------- #
def reset_timer():
    """Reset the timer and session states."""
    global reps, timer, is_timer_running, is_paused
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"{WORK_MIN}:00")
    progress_bar["value"] = 0
    time_label.config(text="Timer", fg=GREEN)
    window.config(bg=YELLOW)
    canvas.config(bg=YELLOW)
    start_button.config(state="normal")
    pause_button.config(state="disabled", text="Pause")
    reps = 0
    is_timer_running = False
    is_paused = False
    update_statistics_display()
    status_bar.config(text="Timer reset. Ready to start!")

def start_timer():
    """Start or continue the Pomodoro timer."""
    global reps, is_timer_running, current_session_start
    if not is_timer_running:
        is_timer_running = True
        start_button.config(state="disabled")
        pause_button.config(state="normal")
        current_session_start = datetime.now()
        reps += 1

        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break_sec)
            update_session_ui("Long Break", RED)
        elif reps % 2 == 0:
            count_down(short_break_sec)
            update_session_ui("Short Break", PINK)
        else:
            count_down(work_sec)
            update_session_ui(f"Work Session {math.ceil(reps/2)}", GREEN)

def toggle_pause():
    """Pause or resume the timer."""
    global is_paused, is_timer_running, remaining_time
    if is_timer_running:
        if not is_paused:
            window.after_cancel(timer)
            pause_button.config(text="Resume")
            time_label.config(text="Paused")
            is_paused = True
            status_bar.config(text="Timer paused.")
        else:
            pause_button.config(text="Pause")
            is_paused = False
            status_bar.config(text="Timer resumed.")
            count_down(remaining_time)

def count_down(count):
    """Countdown mechanism with session management."""
    global timer, is_timer_running, is_paused, remaining_time
    remaining_time = count
    count_min = math.floor(count / 60)
    count_sec = f"{count % 60:02d}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    progress_bar["value"] = ((WORK_MIN * 60 - count) / (WORK_MIN * 60)) * 100

    if count > 0 and not is_paused:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0 and not is_paused:
        complete_session()

def complete_session():
    """Handle session completion and transitions."""
    global is_timer_running, current_session_start
    is_timer_running = False
    start_button.config(state="normal")

    if current_session_start:
        session_type = "Work" if reps % 2 != 0 else "Break"
        completed_sessions.append({
            "type": session_type,
            "duration": WORK_MIN * 60 if session_type == "Work" else SHORT_BREAK_MIN * 60,
            "completed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    reset_timer()

# ---------------------------- HELPER FUNCTIONS ------------------------------- #
def update_statistics_display():
    """Update the statistics display."""
    stats_label.config(text=f"Sessions: {reps//2}\nWork Time: {reps//2 * WORK_MIN} min")

def update_session_ui(session_text, color):
    """Update UI elements for session type."""
    time_label.config(text=session_text, fg=color)
    window.config(bg=color)
    canvas.config(bg=color)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# UI Elements
time_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
time_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"{WORK_MIN}:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
progress_bar.grid(column=1, row=2, pady=(10, 0))

start_button = Button(text="Start", bg=GREEN, fg="white", font=(FONT_NAME, 12), command=start_timer)
start_button.grid(column=0, row=3)

pause_button = Button(text="Pause", bg=PINK, fg="white", font=(FONT_NAME, 12), command=toggle_pause, state="disabled")
pause_button.grid(column=1, row=3)

reset_button = Button(text="Reset", bg=RED, fg="white", font=(FONT_NAME, 12), command=reset_timer)
reset_button.grid(column=2, row=3)

stats_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12))
stats_label.grid(column=1, row=4)

status_bar = Label(text="Ready to start!", bd=1, relief=SUNKEN, anchor=W, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10))
status_bar.grid(column=0, row=5, columnspan=3, sticky="ew")

update_statistics_display()
window.mainloop()