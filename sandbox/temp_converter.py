import tkinter as tk
import ttkbootstrap as ttk

def convert_temperature(input_var, output_var, conversion_type):
    try:
        value = float(input_var.get())
        if conversion_type == "to_celsius":
            result = (value - 32) * 5 / 9
            output_var.set(f"{result:.2f} °C")
        elif conversion_type == "to_fahrenheit":
            result = value * 9 / 5 + 32
            output_var.set(f"{result:.2f} °F")
    except ValueError:
        output_var.set("Invalid Input")

def create_conversion_section(master, title, conversion_type):
    """Creates a section for temperature conversion."""
    # Title Label
    title_label = ttk.Label(master=master, text=title, font="Calibri 18 bold")
    title_label.pack(pady=10)

    # Frame for Entry and Button
    frame = ttk.Frame(master=master)
    input_var = tk.StringVar()
    entry = ttk.Entry(master=frame, textvariable=input_var)
    button = ttk.Button(
        master=frame,
        text="Convert",
        command=lambda: convert_temperature(input_var, output_var, conversion_type),
    )
    entry.pack(side="left", padx=10)
    button.pack(side="left")
    frame.pack(pady=10)

    # Output Label
    output_var = tk.StringVar()
    output_label = ttk.Label(master=master, text="Output:", font="Calibri 16", textvariable=output_var)
    output_label.pack(pady=5)

    return input_var, output_var

# Main Application
def main():
    # Create the main window
    window = ttk.Window(themename="journal")
    window.title("Temperature Converter")
    window.geometry("300x400")

    # Fahrenheit to Celsius Section
    create_conversion_section(window, "Fahrenheit to Celsius", "to_celsius")

    # Celsius to Fahrenheit Section
    create_conversion_section(window, "Celsius to Fahrenheit", "to_fahrenheit")

    # Run the main loop
    window.mainloop()

if __name__ == "__main__":
    main()