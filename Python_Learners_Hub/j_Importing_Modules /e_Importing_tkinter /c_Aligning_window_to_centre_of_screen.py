from tkinter import *

win = Tk()

width = 300
height = 500

sys_width = win.winfo_screenwidth()
sys_height = win.winfo_screenheight()

c_x = int(sys_height/2 - height/2) # Center X position of window on screen
c_y = int(sys_width/2 - width/2)  # Center Y position of window on screen

# Set the position of the window to center of the screen
win.geometry(f"{width}x{height}+{c_x}+{c_y}")

win['bg'] = "yellow"
win.mainloop()
