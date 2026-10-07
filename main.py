import tkinter as tk

# Create the main application window.
root = tk.Tk()
root.title("Calculator")
root.geometry("420x260")
root.minsize(380, 220)

# Main content area that holds all calculator widgets.
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Inputs for the two numbers used in the calculation.
input_frame = tk.Frame(frame)
input_frame.pack(fill="x", pady=(0, 12))

num1 = tk.Entry(input_frame, width=12)
num1.grid(row=0, column=1, sticky="ew")

num2 = tk.Entry(input_frame, width=12)
num2.grid(row=1, column=1, pady=(8, 0), sticky="ew")

input_frame.columnconfigure(1, weight=1)

# Operation selector: each button updates the selected_operation variable.
operation_frame = tk.Frame(frame)
operation_frame.pack(fill="x", pady=(0, 12))

selected_operation = tk.StringVar(value="add")  # Default arithmetic operation.
operation_buttons = [  # Available calculator operations.
    ("Add", "add"),
    ("Subtract", "subtract"),
    ("Multiply", "multiply"),
    ("Divide", "divide"),
]

for index, (label, operation) in enumerate(operation_buttons):
    tk.Button(
        operation_frame,
        text=label,
        command=lambda value=operation: selected_operation.set(value),
    ).grid(row=0, column=index, sticky="ew", padx=4, pady=4)

for index in range(len(operation_buttons)):
    operation_frame.columnconfigure(index, weight=1)

# Displays the result or any validation error to the user.
result_label = tk.Label(frame, text="", anchor="center", wraplength=300)
result_label.pack(fill="x", pady=(0, 12))

# Run the calculation using the current input values and selected operation.
calc_button = tk.Button(
    frame,
    text="Calculate",
    command=lambda: main(num1.get(), num2.get(), selected_operation.get()),
)
calc_button.pack(fill="x")


def main(numone, numtwo, operation):
    """Convert inputs to floats and perform the chosen arithmetic operation."""
    try:
        first = float(numone)
        second = float(numtwo)

        if operation == "add":
            result = first + second
        elif operation == "subtract":
            result = first - second
        elif operation == "multiply":
            result = first * second
        elif operation == "divide":
            result = first / second
        else:
            # Guard against unexpected values.
            result_label.config(text="Select an operation")
            return

        # Use compact formatting for cleaner output such as 2.5 instead of 2.500000.
        result_label.config(text=f"Result: {result:g}")

    except ValueError:
        result_label.config(text="Enter valid numbers")

    except ZeroDivisionError:
        result_label.config(text="Cannot divide by zero")


root.mainloop()
