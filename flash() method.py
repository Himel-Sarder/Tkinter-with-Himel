from tkinter import *

def flash_radiobutton():
    R1.flash() # Flash the Radiobutton

'''
You can adjust the number of flashes and the duration of the flashing effect by providing arguments to the flash() method. 
The default is three flashes. For example:
R1.flash(n=5)  # Flash five times
'''

root = Tk()
var = IntVar()

R1 = Radiobutton(root, text="Flash Me!", variable=var, value=1, selectcolor="yellow", activebackground="lightblue")
R1.pack(anchor=W)

flash_button = Button(root, text="Flash Radiobutton", command=flash_radiobutton)
flash_button.pack(pady=10)

root.mainloop()
