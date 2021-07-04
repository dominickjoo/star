import tkinter as tk

def calculate()

root = tk.Tk()
root.title("Star Battle Solver")

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Number of rows/columns:", padx=3, pady=3)
label.pack()

entry = tk.Entry(frame, width=5)
entry.pack()

root.bind("<Return>", calculate)

root.mainloop()