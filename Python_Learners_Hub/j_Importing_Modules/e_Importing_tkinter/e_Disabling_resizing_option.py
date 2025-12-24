import tkinter as tk

window = tk.Tk() 
window.title( "My Window" )

window.attributes('-alpha',1)

window.config(bg="red") 

window.geometry("300x500+100+100") 

window.resizable(False, False) # makes the window not resizable

window.mainloop()
