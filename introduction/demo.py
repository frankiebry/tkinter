import tkinter as tk # gives us access to the tkinter library
from tkinter import ttk # gives us access to widgets we want to use

# Window
window = tk.Tk() # Create the main window and store it in the variable window
window.title("Miles to Kilometers") # Set the title of the window
window.geometry("300x150") # Set the size of the window

# Run the main event loop
window.mainloop() # Event loop