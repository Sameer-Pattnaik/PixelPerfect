import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor App")
        self.root.geometry("800x600")

        self.image = None
        self.img_display = None

        # UI Elements
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

    def create_widgets(self):
        # Canvas for displaying the image
        self.canvas = tk.Canvas(self.root, bg="gray", width=600, height=400)
        self.canvas.pack(pady=20)

        # Frame for controls
        controls_frame = tk.Frame(self.root)
        controls_frame.pack(pady=10)

        ttk.Button(controls_frame, text="Browse Image", command=self.open_image).grid(row=0, column=0, padx=5)
        ttk.Button(controls_frame, text="Rotate", command=self.rotate_image).grid(row=0, column=1, padx=5)
        ttk.Button(controls_frame, text="Resize", command=self.resize_image).grid(row=0, column=2, padx=5)
        ttk.Button(controls_frame, text="Apply Filter", command=self.apply_filter).grid(row=0, column=3, padx=5)
        ttk.Button(controls_frame, text="Enhance", command=self.enhance_image).grid(row=0, column=4, padx=5)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if file_path:
                self.image.save(file_path)
                messagebox.showinfo("Image Saved", f"Image successfully saved to {file_path}")
        else:
            messagebox.showwarning("No Image", "Please open an image to save.")

    def display_image(self):
        if self.image:
            # Resize image to fit the canvas
            img_resized = self.image.resize((600, 400), Image.Resampling.LANCZOS)
            self.img_display = ImageTk.PhotoImage(img_resized)
            self.canvas.create_image(300, 200, image=self.img_display)

    def rotate_image(self):
        if self.image:
            self.image = self.image.rotate(90, expand=True)
            self.display_image()
        else:
            messagebox.showwarning("No Image", "Please open an image to rotate.")

    def resize_image(self):
        if self.image:
            new_width = tk.simpledialog.askinteger("Resize", "Enter new width:")
            new_height = tk.simpledialog.askinteger("Resize", "Enter new height:")
            if new_width and new_height:
                self.image = self.image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                self.display_image()
        else:
            messagebox.showwarning("No Image", "Please open an image to resize.")

    def apply_filter(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.BLUR)
            self.display_image()
        else:
            messagebox.showwarning("No Image", "Please open an image to apply filters.")

    def enhance_image(self):
        if self.image:
            enhancer = ImageEnhance.Contrast(self.image)
            self.image = enhancer.enhance(1.5)  # Adjust contrast
            self.display_image()
        else:
            messagebox.showwarning("No Image", "Please open an image to enhance.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
