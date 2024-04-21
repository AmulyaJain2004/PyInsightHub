import tkinter as tk

window = tk.Tk() 
window.title( "My Window" )
# window.iconbitmap(r"") # .ico file path

window.attributes('-alpha',1) # adjust transperancy effects

# to set background color, there are 2 ways: -
# 1)
# window['bg'] = "yellow"
# 2) 
window.config(bg="red") #  this is the preferred way of setting bg colfors in  TKinter
# also we can write the color code of anycolor to display

window.geometry("300x500+100+100") # width x height + "+/-" (optional) to default temporary fix the window at the start
window.mainloop()
