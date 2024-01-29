from tkinter import *
root = Tk()
root.title("Himel's Tkinter")
frame = LabelFrame(root, text="Frame", padx=10, pady=10)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't Click") 
b.pack()
root.mainloop()
