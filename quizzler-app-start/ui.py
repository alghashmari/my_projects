from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text= "score: 0", fg="white", bg= THEME_COLOR)
        self.score_label.grid(row=0,column= 1)

        # Canvas for displaying questions
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,
        text="Some Question Text", fill= THEME_COLOR, font= ("Arial", 20 , "bold"))

        self.canvas.grid(row= 1, column= 0, columnspan= 2,pady= 50)

        # True button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.correct_pressed)
        self.true_button.grid(row=2, column=0)
        self.true_image = true_image  # Prevent garbage collection

        # False button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.wrong_pressed)
        self.false_button.grid(row=2, column=1)
        self.false_image = false_image  # Prevent garbage collection

        self.window.mainloop()

    def correct_pressed(self):
        print("Correct button pressed!")

    def wrong_pressed(self):
        print("Wrong button pressed!")