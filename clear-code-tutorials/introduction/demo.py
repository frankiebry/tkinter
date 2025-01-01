# TODO hitting enter should make the button click

import tkinter as tk # Import the tkinter module
# from tkinter import ttk # Gives us access to additional widgets and styling options.
import ttkbootstrap as ttk # Takes ttk widgets and adds more styling options

# Define a function that will be called by the entry button
def convert():
    miles_input = entry_int.get()
    km_output = miles_input * 1.61
    output_string.set(km_output)

# Create the main window
# window = tk.Tk()
window = ttk.Window(themename= 'darkly') # Better styling than tk.Tk()
window.title('Demo')
window.geometry('300x150')

# Bind the Enter key to the convert function
window.bind('<Return>', lambda event: convert())

# Create the title label and place it in the window
title_label = ttk.Label(master = window, text='Miles to Kilometers', font = 'Calibri 24 bold')
title_label.pack() # Place the widget in the window

# Create the input frame and widgets that will be placed in the input frame (which in turn will be placed in the window)
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar() # Create a variable to store the entry value
entry = ttk.Entry(master = input_frame, textvariable = entry_int) # Create an entry widget that will store the value in entryInt
button = ttk.Button(master = input_frame, text = 'Convert', command = convert) # Create a button that calls the convert function
entry.pack(side = 'left', padx = 10) # Place the entry widget in the window with padding on the left and right
button.pack(side = 'left') # Place the button widget next to the entry widget
input_frame.pack(pady = 10) # Place the input frame in the window with padding on the top and bottom

# Create the output frame
output_string = tk.StringVar() # Create a variable to store the output value
output_label = ttk.Label(
    master = window,
    text = 'Output',
    font = 'Calibri 24',
    textvariable=output_string
    )
output_label.pack(pady = 5)

# Run the main loop
window.mainloop()