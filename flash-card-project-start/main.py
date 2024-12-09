import os
import json
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from random import choice
from datetime import datetime
from PIL import Image, ImageTk
import threading
import pyttsx3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configuration and constants
class Config:
    BACKGROUND_COLOR = "#2B2B2B"
    CARD_FRONT_IMAGE = "images/card_front.png"
    CARD_BACK_IMAGE = "images/card_back.png"
    RIGHT_IMAGE = "images/right.png"
    WRONG_IMAGE = "images/wrong.png"
    DATA_FILE = "data/en-ar.csv"
    USER_DATA_DIR = "user_data"
    FLIP_TIME_MS = 3000
    DEFAULT_LANGUAGE = "English"
    TARGET_LANGUAGE = "Arabic"
    APP_TITLE = "Advanced Flashcard Learning System"
    VERSION = "1.0.0"

def ensure_user_data_dir():
    if not os.path.exists(Config.USER_DATA_DIR):
        os.makedirs(Config.USER_DATA_DIR)

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)

def speak(text):
    """Speaks the given text using the TTS engine."""
    threading.Thread(target=tts_engine.say, args=(text,)).start()
    tts_engine.runAndWait()

def clean_data(file_path):
    """
    Cleans the CSV data by removing unwanted entries and standardizing format.

    Args:
        file_path (str): Path to the CSV file containing word pairs

    Returns:
        pandas.DataFrame: Cleaned dataset ready for flashcard use
    """
    try:
        data = pd.read_csv(file_path, encoding='utf-8')
        data.columns = data.columns.str.strip()
        data[Config.TARGET_LANGUAGE] = data[Config.TARGET_LANGUAGE].str.strip()
        data = data.dropna(subset=[Config.DEFAULT_LANGUAGE, Config.TARGET_LANGUAGE])
        data = data[~data[Config.TARGET_LANGUAGE].str.lower().str.contains("loading", na=False)]
        return data
    except FileNotFoundError:
        messagebox.showerror("Data File Not Found",
                             f"The data file '{file_path}' was not found.")
        return pd.DataFrame(columns=[Config.DEFAULT_LANGUAGE, Config.TARGET_LANGUAGE])

class LearningStats:
    """
    Handles tracking and analyzing learning progress.
    """

    def __init__(self, user_id):
        self.user_id = user_id
        self.stats_file = os.path.join(Config.USER_DATA_DIR, f"{self.user_id}_stats.json")
        self.stats = self.load_stats()

    def load_stats(self):
        """Loads existing statistics or creates new ones if none exist."""
        if os.path.exists(self.stats_file):
            with open(self.stats_file, "r", encoding='utf-8') as file:
                return json.load(file)
        else:
            return {
                "total_words_learned": 0,
                "learning_sessions": [],
                "difficult_words": [],
                "daily_progress": {},
                "streak_days": 0
            }

    def save_stats(self):
        """Saves current statistics to file with proper encoding."""
        with open(self.stats_file, "w", encoding='utf-8') as file:
            json.dump(self.stats, file, indent=4, ensure_ascii=False)

    def record_word_learned(self, word, attempts=1):
        """
        Records a successfully learned word and updates progress metrics.

        Args:
            word (dict): The word pair that was learned
            attempts (int): Number of attempts taken to learn the word
        """
        today = datetime.now().strftime("%Y-%m-%d")
        self.stats["daily_progress"].setdefault(today, 0)
        self.stats["daily_progress"][today] += 1
        self.stats["total_words_learned"] += 1
        self.update_streak(today)
        self.save_stats()

    def update_streak(self, today):
        """Updates the learning streak based on consistency."""
        dates = sorted(self.stats["daily_progress"].keys())
        if dates:
            last_date = datetime.strptime(dates[-1], "%Y-%m-%d")
            today_date = datetime.strptime(today, "%Y-%m-%d")
            days_diff = (today_date - last_date).days
            if days_diff == 1:
                self.stats["streak_days"] += 1
            elif days_diff > 1:
                self.stats["streak_days"] = 1
        else:
            self.stats["streak_days"] = 1

    def record_difficult_word(self, word):
        """Adds a word to the difficult words list for extra practice."""
        if word not in self.stats["difficult_words"]:
            self.stats["difficult_words"].append(word)
            self.save_stats()

class FlashcardApp:
    """
    Main application class that handles the UI and learning mechanics.
    """

    def __init__(self):
        ensure_user_data_dir()
        self.window = tk.Tk()
        self.window.title(f"{Config.APP_TITLE} v{Config.VERSION}")
        self.window.config(padx=50, pady=50, bg=Config.BACKGROUND_COLOR)

        # User authentication
        self.user_id = None
        self.user_settings = {}
        self.login_window()

    def login_window(self):
        """Creates a login window for user authentication."""
        login_win = tk.Toplevel(self.window)
        login_win.title("User Login")
        login_win.geometry("300x200")
        login_win.config(padx=20, pady=20)

        tk.Label(login_win, text="Enter your username:").pack(pady=10)
        username_entry = tk.Entry(login_win)
        username_entry.pack()

        def proceed():
            username = username_entry.get().strip()
            if username:
                self.user_id = username
                self.load_user_settings()
                self.stats = LearningStats(self.user_id)
                self.word_list = self.load_data()
                self.current_word = None
                self.current_attempts = 0
                self.review_mode = False
                login_win.destroy()
                self.setup_ui()
                self.setup_menu()
                self.update_card()
            else:
                messagebox.showwarning("Input Required", "Please enter a username.")

        tk.Button(login_win, text="Login", command=proceed).pack(pady=20)
        login_win.grab_set()
        self.window.wait_window(login_win)

    def load_user_settings(self):
        """Loads user-specific settings."""
        settings_file = os.path.join(Config.USER_DATA_DIR, f"{self.user_id}_settings.json")
        if os.path.exists(settings_file):
            with open(settings_file, "r", encoding='utf-8') as file:
                self.user_settings = json.load(file)
        else:
            self.user_settings = {
                "flip_time_ms": Config.FLIP_TIME_MS,
                "dark_mode": False
            }
            self.save_user_settings()

    def save_user_settings(self):
        """Saves user-specific settings."""
        settings_file = os.path.join(Config.USER_DATA_DIR, f"{self.user_id}_settings.json")
        with open(settings_file, "w", encoding='utf-8') as file:
            json.dump(self.user_settings, file, indent=4, ensure_ascii=False)

    def load_data(self):
        """Loads and initializes the flashcard data."""
        progress_file = os.path.join(Config.USER_DATA_DIR, f"{self.user_id}_progress.json")
        if os.path.exists(progress_file):
            with open(progress_file, "r", encoding='utf-8') as file:
                return json.load(file)
        else:
            data = clean_data(Config.DATA_FILE)
            word_list = data.to_dict(orient="records")
            with open(progress_file, "w", encoding='utf-8') as file:
                json.dump(word_list, file, ensure_ascii=False, indent=4)
            return word_list

    def save_progress(self):
        """Saves current learning progress."""
        progress_file = os.path.join(Config.USER_DATA_DIR, f"{self.user_id}_progress.json")
        with open(progress_file, "w", encoding='utf-8') as file:
            json.dump(self.word_list, file, ensure_ascii=False, indent=4)

    def setup_menu(self):
        """Creates the application menu bar with various options."""
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Settings", command=self.open_settings)
        file_menu.add_command(label="Reset Progress", command=self.reset_progress)
        file_menu.add_command(label="Export Statistics", command=self.export_stats)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)

        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Show Statistics", command=self.show_statistics)
        view_menu.add_command(label="Show Difficult Words", command=self.show_difficult_words)

    def setup_ui(self):
        """Sets up the main user interface components."""
        # Main frame
        self.content_frame = tk.Frame(self.window, bg=Config.BACKGROUND_COLOR)
        self.content_frame.grid(row=0, column=0, sticky="nsew")

        # Statistics area
        self.setup_stats_frame(self.content_frame)

        # Flashcard area
        self.setup_flashcard_area(self.content_frame)

        # Control buttons
        self.setup_control_buttons(self.content_frame)

    def setup_stats_frame(self, parent):
        """Creates the statistics display area."""
        self.stats_frame = tk.Frame(parent, bg=Config.BACKGROUND_COLOR)
        self.stats_frame.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Progress display
        self.progress_var = tk.StringVar()
        self.update_progress_label()
        progress_label = tk.Label(self.stats_frame, textvariable=self.progress_var,
                                  bg=Config.BACKGROUND_COLOR, fg='white', font=("Arial", 12))
        progress_label.pack()

        # Streak display
        self.streak_var = tk.StringVar()
        self.update_streak_label()
        streak_label = tk.Label(self.stats_frame, textvariable=self.streak_var,
                                bg=Config.BACKGROUND_COLOR, fg='white', font=("Arial", 12))
        streak_label.pack()

    def setup_flashcard_area(self, parent):
        """Creates the main flashcard display area."""
        self.canvas = tk.Canvas(parent, width=800, height=526,
                                bg=Config.BACKGROUND_COLOR, highlightthickness=0)

        # Load images using PIL for better compatibility
        self.card_front_image = ImageTk.PhotoImage(Image.open(Config.CARD_FRONT_IMAGE))
        self.card_back_image = ImageTk.PhotoImage(Image.open(Config.CARD_BACK_IMAGE))

        self.card_background = self.canvas.create_image(400, 263, image=self.card_front_image)
        self.language_text = self.canvas.create_text(400, 150, text=Config.DEFAULT_LANGUAGE,
                                                     font=("Arial", 40, "italic"), fill='black')
        self.word_text = self.canvas.create_text(400, 263, text="Word",
                                                 font=("Arial", 60, "bold"), fill='black')
        self.canvas.grid(row=1, column=0, columnspan=2)

    def setup_control_buttons(self, parent):
        """Creates the control buttons for user interaction."""
        button_frame = tk.Frame(parent, bg=Config.BACKGROUND_COLOR)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)

        # Load button images
        self.right_image = ImageTk.PhotoImage(Image.open(Config.RIGHT_IMAGE))
        self.wrong_image = ImageTk.PhotoImage(Image.open(Config.WRONG_IMAGE))

        # Create the buttons
        style = ttk.Style()
        style.configure("Custom.TButton", padding=10)

        # Define button configurations
        buttons = [
            ("Mark Difficult", self.mark_difficult, "Mark this word as difficult for extra practice", None),
            (None, self.mark_wrong, "I got this wrong, show me again", self.wrong_image),
            (None, self.mark_known, "I know this word, remove from practice", self.right_image),
            ("Pronounce", self.pronounce_word, "Hear the pronunciation of the word", None)
        ]

        for i, (text, command, tooltip, image) in enumerate(buttons):
            btn = ttk.Button(
                button_frame,
                text=text if text else "",
                image=image,
                command=command,
                style="Custom.TButton"
            )
            btn.grid(row=0, column=i, padx=5)
            self.create_tooltip(btn, tooltip)

    def create_tooltip(self, widget, text):
        """Creates a hovering tooltip for a widget."""

        def on_enter(event):
            self.tooltip = tk.Toplevel()
            self.tooltip.wm_overrideredirect(True)
            x, y = event.x_root + 10, event.y_root + 10
            self.tooltip.wm_geometry(f"+{x}+{y}")
            label = tk.Label(self.tooltip, text=text, justify=tk.LEFT,
                             background="#ffffe0", relief=tk.SOLID, borderwidth=1)
            label.pack()

        def on_leave(event):
            if self.tooltip:
                self.tooltip.destroy()

        widget.bind('<Enter>', on_enter)
        widget.bind('<Leave>', on_leave)

    def update_card(self):
        """Updates the flashcard with a new word."""
        if not self.word_list:
            self.show_completion_message()
            return

        self.current_word = choice(self.word_list)
        self.canvas.itemconfig(self.card_background, image=self.card_front_image)
        self.canvas.itemconfig(self.language_text, text=Config.DEFAULT_LANGUAGE, fill="black")
        self.canvas.itemconfig(self.word_text, text=self.current_word[Config.DEFAULT_LANGUAGE], fill="black")
        flip_time = self.user_settings.get("flip_time_ms", Config.FLIP_TIME_MS)
        self.flip_timer = self.window.after(flip_time, self.flip_card)

    def flip_card(self):
        """Flips the flashcard to show the translation."""
        self.canvas.itemconfig(self.card_background, image=self.card_back_image)
        self.canvas.itemconfig(self.language_text, text=Config.TARGET_LANGUAGE, fill="white")
        self.canvas.itemconfig(self.word_text, text=self.current_word[Config.TARGET_LANGUAGE], fill="white")

    def mark_difficult(self):
        """Handles marking a word as difficult."""
        if self.current_word:
            self.stats.record_difficult_word(self.current_word)
            self.current_attempts += 1
            self.update_card()

    def mark_wrong(self):
        """Handles incorrect responses."""
        if self.current_word:
            self.current_attempts += 1
            if self.current_attempts >= 3:
                self.stats.record_difficult_word(self.current_word)
            self.update_card()

    def mark_known(self):
        """Handles correct responses."""
        if self.current_word:
            self.stats.record_word_learned(self.current_word, self.current_attempts)
            self.word_list.remove(self.current_word)
            self.save_progress()
            self.current_attempts = 0
            self.update_card()
            self.update_progress_label()
            self.update_streak_label()

    def pronounce_word(self):
        """Pronounces the current word."""
        if self.current_word:
            text = self.current_word[Config.DEFAULT_LANGUAGE]
            speak(text)

    def update_progress_label(self):
        """Updates the progress display."""
        total_words = len(self.word_list) + self.stats.stats["total_words_learned"]
        progress = (self.stats.stats["total_words_learned"] / total_words) * 100 if total_words else 100
        self.progress_var.set(
            f"Progress: {progress:.1f}% ({self.stats.stats['total_words_learned']}/{total_words} words)")

    def update_streak_label(self):
        """Updates the streak display."""
        self.streak_var.set(f"Learning streak: {self.stats.stats['streak_days']} days")

    def reset_progress(self):
        """Resets all progress after confirmation."""
        if messagebox.askyesno("Reset Progress", "Are you sure you want to reset all progress?"):
            self.word_list = clean_data(Config.DATA_FILE).to_dict(orient="records")
            self.stats = LearningStats(self.user_id)
            self.save_progress()
            self.update_card()
            self.update_progress_label()
            self.update_streak_label()

    def export_stats(self):
        """Exports learning statistics to a file."""
        export_file = os.path.join(Config.USER_DATA_DIR, f"{self.user_id}_stats_export.json")
        with open(export_file, "w", encoding='utf-8') as file:
            json.dump({
                "statistics": self.stats.stats,
                "current_progress": len(self.word_list),
                "export_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }, file, ensure_ascii=False, indent=4)
        messagebox.showinfo("Export Complete",
                            f"Statistics have been exported to {export_file}")

    def show_statistics(self):
        """Displays learning statistics in a graphical window."""
        stats_window = tk.Toplevel(self.window)
        stats_window.title("Learning Statistics")
        stats_window.geometry("600x400")

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

        # Daily progress plot
        dates = list(self.stats.stats["daily_progress"].keys())
        words = list(self.stats.stats["daily_progress"].values())
        ax1.plot(dates, words, marker='o')
        ax1.set_title("Daily Learning Progress")
        ax1.set_xlabel("Date")
        ax1.set_ylabel("Words Learned")
        plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')

        # Overall progress pie chart
        total_words = len(self.word_list) + self.stats.stats["total_words_learned"]
        words_learned = self.stats.stats["total_words_learned"]
        ax2.pie([words_learned, total_words - words_learned],
                labels=['Learned', 'Remaining'],
                autopct='%1.1f%%',
                startangle=140)
        ax2.set_title("Overall Progress")

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=stats_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def show_difficult_words(self):
        """Shows a list of words marked as difficult."""
        difficult_window = tk.Toplevel(self.window)
        difficult_window.title("Difficult Words")
        difficult_window.geometry("400x300")

        scrollbar = ttk.Scrollbar(difficult_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(difficult_window, yscrollcommand=scrollbar.set)
        for word in self.stats.stats["difficult_words"]:
            listbox.insert(tk.END, f"{word[Config.DEFAULT_LANGUAGE]} - {word[Config.TARGET_LANGUAGE]}")

        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)

    def show_completion_message(self):
        """Displays a message when all words are learned."""
        self.canvas.itemconfig(self.language_text, text="Congratulations!", fill="black")
        self.canvas.itemconfig(self.word_text, text="You've learned all the words!", fill="black")

    def open_settings(self):
        """Opens the settings window."""
        settings_win = tk.Toplevel(self.window)
        settings_win.title("Settings")
        settings_win.geometry("300x200")
        settings_win.config(padx=20, pady=20)

        tk.Label(settings_win, text="Flip Time (ms):").grid(row=0, column=0, pady=10, sticky='w')
        flip_time_entry = tk.Entry(settings_win)
        flip_time_entry.insert(0, str(self.user_settings.get("flip_time_ms", Config.FLIP_TIME_MS)))
        flip_time_entry.grid(row=0, column=1, pady=10)

        dark_mode_var = tk.BooleanVar(value=self.user_settings.get("dark_mode", False))
        tk.Checkbutton(settings_win, text="Dark Mode", variable=dark_mode_var).grid(row=1, column=0, columnspan=2)

        def save_settings():
            try:
                flip_time = int(flip_time_entry.get())
                self.user_settings["flip_time_ms"] = flip_time
                self.user_settings["dark_mode"] = dark_mode_var.get()
                self.save_user_settings()
                messagebox.showinfo("Settings Saved", "Your settings have been updated.")
                settings_win.destroy()
            except ValueError:
                messagebox.showerror("Invalid Input", "Flip time must be an integer.")

        tk.Button(settings_win, text="Save", command=save_settings).grid(row=2, column=0, columnspan=2, pady=20)

    def run(self):
        """Runs the Tkinter main loop."""
        self.window.mainloop()

def main():
    app = FlashcardApp()
    app.run()

if __name__ == "__main__":
    main()