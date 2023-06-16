import tkinter as tk

def calculate_addition():
    numberA = entryA.get()
    numberB = entryB.get()

    if numberA.isdigit() and numberB.isdigit():
        numberA = int(numberA)
        numberB = int(numberB)
        addition = numberA + numberB
        result_label.config(text=f"{numberA} plus {numberB} equals {addition}")
    else:
        result_label.config(text="I assumed you were smart... it says \n***NUMBERS***")

# Create the main window
window = tk.Tk()

# Create and place the entry fields
entryA_label = tk.Label(window, text="Type a number:")
entryA_label.pack()
entryA = tk.Entry(window)
entryA.pack()

entryB_label = tk.Label(window, text="Type another number:")
entryB_label.pack()
entryB = tk.Entry(window)
entryB.pack()

# Create and place the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_addition)
calculate_button.pack()

# Create and place the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
