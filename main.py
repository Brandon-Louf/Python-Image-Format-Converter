from PIL import Image
import os

# User input file
input_file = "image.png"

# Tries to open the input file if it exists as an image file
try:
    with Image.open(input_file) as img:
        input_format = img.format
        print(f"Input Image Format is {input_format}")

except IOError:
    print("Error: Invalid image file.")