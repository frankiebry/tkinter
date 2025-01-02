# Tutorial on widgets

import tkinter as tk
from tkinter import ttk

def button_func():
    print('Button clicked')
    
def hello_func():
    print('Hello!')

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# tk.txt
text_1 = tk.Text(master = window) # multi-line text input
text_1.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# ttk label
label_2 = ttk.Label(master = window, text = 'my label')
label_2.pack()

# ttk button
button = ttk.Button(master = window, text = 'Click me!', command = button_func)
button.pack()

# ttk hello button
# hello_button = ttk.Button(master = window, text = 'Hello?', command = hello_func)
hello_button = ttk.Button(master = window, text = 'Hello?', command = lambda:print('hello there!'))
hello_button.pack()

# run
window.mainloop()
print('Hello World')