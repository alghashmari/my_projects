from tkinter import *


def button_clicked():
    # Access the entry widget's value and calculate the result
    result = float(entry.get()) * 1.609344
    result = round(result)
    answer_label.config(text=result)

# Windows
window = Tk()
window.title("My First GUI")
window.config(padx=20, pady=20)

# Labels
mile_label = Label(text="Miles")
mile_label.grid(column=1, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

answer_label = Label(text="0")  # Default text for the label
answer_label.grid(column=1, row=1)

kilo_label = Label(text="km")
kilo_label.grid(column=2, row=1)

# Entry
entry = Entry(width=10)  # Define the entry widget
entry.grid(column=1, row=0)

# Button
button = Button(text="Convert", command=button_clicked)  # Pass the function reference
button.grid(column=1, row=2)

# Keep the window running
window.mainloop()