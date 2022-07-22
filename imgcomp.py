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
        self.path_request = ttk.Label(self, text = 'Image Prefix')
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

        # load images
        self.load_images()

        # display image
        img_htw_ratio = self.comp_img.size[1] / self.comp_img.size[0]
        self.geometry('600x' + str(int(400 * img_htw_ratio) + 150))
        self.img_small_size = (400, int(400 * img_htw_ratio))
        self.comp_img_resize = self.comp_img.resize(self.img_small_size)
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

        # function text
        self.red_function_label = ttk.Label(
            self.input_frame, text = 'Red Function')
        self.green_function_label = ttk.Label(
            self.input_frame, text = 'Green Function')
        self.blue_function_label = ttk.Label(
            self.input_frame, text = 'Blue Function')

        self.red_function_label.grid(row = 0, column = 2)
        self.green_function_label.grid(row = 1, column = 2)
        self.blue_function_label.grid(row = 2, column = 2)

        # function value
        self.red_function = tk.StringVar()
        self.green_function = tk.StringVar()
        self.blue_function = tk.StringVar()

        self.red_function_entry = ttk.Entry(
            self.input_frame, textvariable = self.red_function)
        self.green_function_entry = ttk.Entry(
            self.input_frame, textvariable = self.green_function)
        self.blue_function_entry = ttk.Entry(
            self.input_frame, textvariable = self.blue_function)

        self.red_function_entry.grid(row = 0, column = 3)
        self.green_function_entry.grid(row = 1, column = 3)
        self.blue_function_entry.grid(row = 2, column = 3)

        # cap text
        self.red_cap_label = ttk.Label(
            self.input_frame, text = 'Red Cap')
        self.green_cap_label = ttk.Label(
            self.input_frame, text = 'Green Cap')
        self.blue_cap_label = ttk.Label(
            self.input_frame, text = 'Blue Cap')

        self.red_cap_label.grid(row = 0, column = 4)
        self.green_cap_label.grid(row = 1, column = 4)
        self.blue_cap_label.grid(row = 2, column = 4)

        # cap value
        self.red_cap = tk.IntVar()
        self.green_cap = tk.IntVar()
        self.blue_cap = tk.IntVar()

        self.red_cap_entry = ttk.Entry(
            self.input_frame, textvariable = self.red_cap)
        self.green_cap_entry = ttk.Entry(
            self.input_frame, textvariable = self.green_cap)
        self.blue_cap_entry = ttk.Entry(
            self.input_frame, textvariable = self.blue_cap)

        self.red_cap_entry.grid(row = 0, column = 5)
        self.green_cap_entry.grid(row = 1, column = 5)
        self.blue_cap_entry.grid(row = 2, column = 5)

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

        self.comp_img = Image.new('RGB', self.red_img.size, (0, 0, 0))
        self.comp_pixels = self.comp_img.load()

    def make_composite(self):
        red_cutoff_val = self.red_cutoff.get() 
        green_cutoff_val = self.green_cutoff.get() 
        blue_cutoff_val = self.blue_cutoff.get() 

        red_cap_val = self.red_cap.get()
        green_cap_val = self.green_cap.get()
        blue_cap_val = self.blue_cap.get()

        red_function_str = self.red_function.get()
        green_function_str = self.green_function.get()
        blue_function_str = self.blue_function.get()

        for i in range(self.comp_img.size[0]):
            for j in range(self.comp_img.size[1]):
                index = j + i * self.comp_img.size[1]

                red = 0
                green = 0
                blue = 0

                r = self.red_pixels[i, j][0]
                g = self.green_pixels[i, j][1]
                b = self.blue_pixels[i, j][2]

                if r > red_cutoff_val:
                    red = eval(red_function_str)
                    if red > red_cap_val:
                        red = red_cap_val

                if g > green_cutoff_val:
                    green = eval(green_function_str)
                    if green > green_cap_val:
                        green = green_cap_val

                if b > blue_cutoff_val:
                    blue = eval(blue_function_str)
                    if blue > blue_cap_val:
                        blue = blue_cap_val

                self.comp_pixels[i, j] = (red, green, blue)

        self.comp_img_resize = self.comp_img.resize(self.img_small_size)
        self.tkImg = ImageTk.PhotoImage(self.comp_img_resize)
        self.img_display.configure(image = self.tkImg)

if __name__ == '__main__':
    app = App()
    app.mainloop()

