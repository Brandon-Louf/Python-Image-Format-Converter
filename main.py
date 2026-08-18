from PIL import Image
import os

# User input file
input_file = "image.png"
selected_format = 0

# Tries to open the input file if it exists as an image file
try:
    with Image.open(input_file) as img:
        # The format type of the image (PNG, PDF, ect.)
        input_format = img.format
        print(f"Input image format is {input_format}")

        output_format = ['PNG', 'JPEG', 'PDF', 'WEBP']
        print(f"What format do you want to convert {input_file} to?")

        # Prints the elements in the tuple in order
        for i, formats, in enumerate(output_format):
            print(f"{i + 1}. {formats} ")

        selected_format = int(input("Enter a number: "))

        # Will ask again for a number if the input is invalid
        while (not 1 <= selected_format <= len(output_format)):
            selected_format = int(input("Please enter a listed number: "))


except IOError:
    print("Error: Invalid image file.")