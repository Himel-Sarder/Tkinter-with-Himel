from tkinter import Tk, Button, Canvas, filedialog, Toplevel
from PIL import Image, ImageTk

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        show_image(file_path)

def show_image(file_path):
    image = Image.open(file_path)
    tk_image = ImageTk.PhotoImage(image)

    # Create a new Toplevel window to display the image
    image_window = Toplevel(root)
    image_window.title("Image Viewer")

    canvas = Canvas(image_window, width=image.width, height=image.height)
    canvas.pack()

    # Display the image on the canvas
    canvas.create_image(0, 0, anchor="nw", image=tk_image)

# Create the main window
root = Tk()
root.title("Image Viewer")

# Create a button to open the file dialog
button = Button(root, text="Open Image", command=open_file_dialog)
button.pack(pady=20)

root.mainloop()
