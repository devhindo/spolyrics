import tkinter as tk
from spotify import auth
root = tk.Tk()


t = "ahmed"
l = tk.Label(root, text=t)

l.pack()    

root.mainloop()

auth()