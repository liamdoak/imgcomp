# imgcomp
A program to combine the red, green, and blue components of images taken with a
color fluorescence microscope.

## Installation
This program uses the Pillow library for image loading and manipulation. 
To install, run: `pip install Pillow`

## Usage
To run the program, run the command: `python imgcomp.py`

imgcomp expects three images with the format "*prefix*_TX RED" for the red,
"*prefix*_GFP" for the green, and "*prefix*_DAPI" for the blue. Its output will
be "*prefix*_Composite". Enter the *prefix* into the "Image Prefix" field and
click "Load" to load the images.

Once the images are loaded, there are nine fields which can be filled in,
divided into red, green, and blue. The cutoff fields determine the minimum color
value a pixel can have without being set to zero. The function fields determines
how to scale the current color values after the cutoff. `r`, `g`, and `b` should
be used to represent the current color value, and any inputed expression should
be valid python code. The cap fields represent the highest value the function
output can be, and any function output higher than that value is capped at that
value.

To update the currently displayed picture, click "Update", and to save the
current picture, click "Save"
