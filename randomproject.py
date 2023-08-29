import tkinter as tk
from tkinter import ttk
import random

def generate_random_number():
    num_digits = int(entry.get())
    min_value = 10 ** (num_digits - 1)
    max_value = (10 ** num_digits) - 1
    random_number = random.randint(min_value, max_value)
    result_label.config(text=f"Random Number: {random_number}")

# Create the main window
root = tk.Tk()
root.title("Random Number Generator")

# Create a style object for ttk widgets
style = ttk.Style()
style.configure("TButton", padding=10, font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 14))

# Create GUI components using ttk
label = ttk.Label(root, text="Enter number of digits:")
entry = ttk.Entry(root, font=("Helvetica", 14))
generate_button = ttk.Button(root, text="Generate Random Number", command=generate_random_number)
result_label = ttk.Label(root, text="Random Number: ", font=("Helvetica", 14))

# Place components using grid layout
label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, columnspan=2, padx=10, pady=20)
result_label.grid(row=2, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
