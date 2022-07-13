import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.path = ""
        self.title('Image Composition')
        self.geometry('400x100')
        self.create_widgets()
        self.red_cutoff = tk.IntVar()
        self.green_cutoff = tk.IntVar()
        self.blue_cutoff = tk.IntVar()

    def create_widgets(self):
        self.path_request = ttk.Label(self, text = 'Image Path')
        self.path_request.pack()
        
        self.path_var = tk.StringVar()
        self.path_entry = ttk.Entry(self, textvariable = self.path_var,
                                    width = 50)
        self.path_entry.pack()

        self.load = ttk.Button(self, text = "Load", command = self.set_path)
        self.load.pack()

    def set_path(self):
        self.path_prefix = self.path_var.get()
        self.next_widgets()

    def next_widgets(self):
        # destroy old widgets
        self.path_request.destroy()
        self.path_entry.destroy()
        self.load.destroy()

        self.load_images()
        self.make_composite_first()

        # display image
        self.geometry('300x450')
        self.comp_img_resize = self.comp_img.resize((300, 300))
        self.tkImg = ImageTk.PhotoImage(self.comp_img_resize)

        self.img_display = ttk.Label(self, image = self.tkImg)
        self.img_display.grid(row = 0, column = 0)

        # frame for input
        self.input_frame = ttk.Frame(self)
        self.input_frame.grid(row = 1, column = 0)

        # cut off value text
        self.red_cutoff_label = ttk.Label(
            self.input_frame, text = 'Red Cutoff')
        self.green_cutoff_label = ttk.Label(
            self.input_frame, text = 'Green Cutoff')
        self.blue_cutoff_label = ttk.Label(
            self.input_frame, text = 'Blue Cutoff')

        self.red_cutoff_label.grid(row = 0, column = 0)
        self.green_cutoff_label.grid(row = 1, column = 0)
        self.blue_cutoff_label.grid(row = 2, column = 0)

        # cut off values
        self.red_cutoff = tk.IntVar()
        self.green_cutoff = tk.IntVar()
        self.blue_cutoff = tk.IntVar()

        self.red_cutoff_entry = ttk.Entry(
            self.input_frame, textvariable = self.red_cutoff)
        self.green_cutoff_entry = ttk.Entry(
            self.input_frame, textvariable = self.green_cutoff)
        self.blue_cutoff_entry = ttk.Entry(
            self.input_frame, textvariable = self.blue_cutoff)

        self.red_cutoff_entry.grid(row = 0, column = 1)
        self.green_cutoff_entry.grid(row = 1, column = 1)
        self.blue_cutoff_entry.grid(row = 2, column = 1)

        # update button
        self.update_button = ttk.Button(
            self, text = "Update", command = self.update)
        self.update_button.grid(row = 2, column = 0)

        # save button
        self.save_button = ttk.Button(
            self, text = "Save", command = self.save)
        self.save_button.grid(row = 3, column = 0)

    def update(self):
        self.make_composite()

    def save(self):
        self.comp_img_tiff = self.comp_img.convert('P')
        self.comp_img_tiff.save(self.path_prefix + '_Composite.tiff')

    def load_images(self):
        self.red_img = Image.open(
            self.path_prefix + "_TX RED.tiff").convert('RGB')
        self.red_pixels = self.red_img.load()

        self.green_img = Image.open(
            self.path_prefix + "_GFP.tiff").convert('RGB')
        self.green_pixels = self.green_img.load()

        self.blue_img = Image.open(
            self.path_prefix + "_DAPI.tiff").convert('RGB')
        self.blue_pixels = self.blue_img.load()

    def make_composite_first(self):
        self.red_pixels_a = []
        self.green_pixels_a = []
        self.blue_pixels_a = []

        for i in range(self.red_img.size[0]):
            for j in range(self.red_img.size[1]):
                if self.red_pixels[i, j][0] <= self.red_cutoff.get():
                    self.red_pixels_a += [(0, 0, 0)]
                else:
                    self.red_pixels_a += [(255, 0, 0)]

        for i in range(self.green_img.size[0]):
            for j in range(self.green_img.size[1]):
                if self.green_pixels[i, j][1] <= self.green_cutoff.get():
                    self.green_pixels_a += [(0, 0, 0)]
                else:
                    self.green_pixels_a += [(0, 255, 0)]

        for i in range(self.blue_img.size[0]):
            for j in range(self.blue_img.size[1]):
                if self.blue_pixels[i, j][2] <= self.blue_cutoff.get():
                    self.blue_pixels_a += [(0, 0, 0)]
                else:
                    self.blue_pixels_a += [(0, 0, 255)]

        self.comp_img = Image.new('RGB', self.red_img.size, (0, 0, 0))
        self.comp_pixels = self.comp_img.load()

        for i in range(self.red_img.size[0]):
            for j in range(self.red_img.size[1]):
                index = j + i * self.comp_img.size[1]
                red = self.red_pixels_a[index][0]
                green = self.green_pixels_a[index][1]
                blue = self.blue_pixels_a[index][2]
                self.comp_pixels[i, j] = (red, green, blue)

    def make_composite(self):
        for i in range(self.red_img.size[0]):
            for j in range(self.red_img.size[1]):
                index = j + i * self.red_img.size[1]
                if self.red_pixels[i, j][0] <= self.red_cutoff.get():
                    self.red_pixels_a[index] = (0, 0, 0)
                else:
                    self.red_pixels_a[index] = (255, 0, 0)

        for i in range(self.green_img.size[0]):
            for j in range(self.green_img.size[1]):
                index = j + i * self.green_img.size[1]
                if self.green_pixels[i, j][1] <= self.green_cutoff.get():
                    self.green_pixels_a[index] = (0, 0, 0)
                else:
                    self.green_pixels_a[index] = (0, 255, 0)

        for i in range(self.blue_img.size[0]):
            for j in range(self.blue_img.size[1]):
                index = j + i * self.blue_img.size[1]
                if self.blue_pixels[i, j][2] <= self.blue_cutoff.get():
                    self.blue_pixels_a[index] = (0, 0, 0)
                else:
                    self.blue_pixels_a[index] = (0, 0, 255)

        self.comp_img = Image.new('RGB', self.red_img.size, (0, 0, 0))
        self.comp_pixels = self.comp_img.load()

        for i in range(self.red_img.size[0]):
            for j in range(self.red_img.size[1]):
                index = j + i * self.comp_img.size[1]
                red = self.red_pixels_a[index][0]
                green = self.green_pixels_a[index][1]
                blue = self.blue_pixels_a[index][2]
                self.comp_pixels[i, j] = (red, green, blue)

        self.comp_img_resize = self.comp_img.resize((300, 300))
        self.tkImg = ImageTk.PhotoImage(self.comp_img_resize)
        self.img_display.configure(image = self.tkImg)

if __name__ == '__main__':
    app = App()
    app.mainloop()
