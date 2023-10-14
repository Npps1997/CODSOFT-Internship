import tkinter as tk
from tkinter import ttk

# Arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x / y

# Function to perform the calculation
def calculate():
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    choice = operation_var.get()

    try:
        num1 = float(num1)
        num2 = float(num2)

        if choice == 1:
            result.set(add(num1, num2))
        elif choice == 2:
            result.set(subtract(num1, num2))
        elif choice == 3:
            result.set(multiply(num1, num2))
        elif choice == 4:
            result.set(divide(num1, num2))
    except ValueError:
        result.set("Please enter valid numbers")

def clear_inputs():
    entry_num1.delete(0, 'end')
    entry_num2.delete(0, 'end')
    result.set("")

# Main window
window = tk.Tk()
window.title("Calculator")

# Styling
style = ttk.Style()
style.configure('TButton', padding=(10, 5))
style.configure('TRadiobutton', padding=(10, 5))

# Background color and padding
window.configure(bg="#f0f0f0")
window.geometry("300x400")

# Input fields and labels
frame = tk.Frame(window, bg="#f0f0f0")
frame.pack(pady=10)

label_num1 = tk.Label(frame, text="Enter Number 1:", bg="#f0f0f0", fg="black")
label_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(frame, bg="white", fg="black")
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(frame, text="Enter Number 2:", bg="#f0f0f0", fg="black")
label_num2.grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(frame, bg="white", fg="black")
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Radio buttons for operation choice
label_operation = tk.Label(frame, text="Select Operation:", bg="#f0f0f0", fg="black")
label_operation.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

operation_var = tk.IntVar()
operation_var.set(1)  # Default to Addition
operations = [("Addition", 1), ("Subtraction", 2), ("Multiplication", 3), ("Division", 4)]
for i, (text, value) in enumerate(operations):
    operation_radio = ttk.Radiobutton(frame, text=text, variable=operation_var, value=value, style='TRadiobutton')
    operation_radio.grid(row=3 + i, column=0, columnspan=2, padx=10, pady=5)

# Calculate and clear buttons
calculate_button = ttk.Button(frame, text="Calculate", command=calculate, style='TButton')
calculate_button.grid(row=7, column=0, columnspan=1, padx=10, pady=10)

clear_button = ttk.Button(frame, text="Clear", command=clear_inputs, style='TButton')
clear_button.grid(row=7, column=1, columnspan=1, padx=10, pady=10)

# Result label and display
result = tk.StringVar()
result_label = tk.Label(frame, text="Result:", bg="#f0f0f0", fg="black")
result_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

result_display = tk.Label(frame, textvariable=result, bg="white", fg="black")
result_display.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

# Center the window
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_width()
window_height = window.winfo_height()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()