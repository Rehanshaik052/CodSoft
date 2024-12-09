import tkinter as tk
from tkinter import messagebox

def calculate():
    try:        
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return

        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")

# Input for first number
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(root, width=20)
entry_num1.pack(pady=5)

# Input for second number
label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(root, width=20)
entry_num2.pack(pady=5)

# Operation selection
operation_var = tk.StringVar()
operation_var.set('+')  # Default operation

label_operation = tk.Label(root, text="Choose an operation:")
label_operation.pack(pady=5)

# Correctly set operation values
operations = [
    ('Addition (+)', '+'),
    ('Subtraction (-)', '-'),
    ('Multiplication (*)', '*'),
    ('Division (/)', '/')
]

for text, value in operations:
    tk.Radiobutton(root, text=text, variable=operation_var, value=value).pack(anchor='w')

# Calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
label_result.pack(pady=10)

# Run the application
root.mainloop()


