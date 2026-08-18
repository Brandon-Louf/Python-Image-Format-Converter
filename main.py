from PIL import Image
import os

# User input file
input_file = "image.png"
user_choice = 0

# Tries to open the input file if it exists as an image file
try:
    with Image.open(input_file) as img:
        # The format type of the image (PNG, PDF, ect.)
        input_format = img.format
        print(f"Input image format is {input_format}")

        available_formats = ['PNG', 'JPEG', 'PDF', 'WEBP']
        print(f"What format do you want to convert {input_file} to?")

        # Prints the elements in the tuple in order
        for i, formats, in enumerate(available_formats):
            print(f"{i + 1}. {formats} ")

        user_choice = int(input("Enter a number: "))

        # Will ask again for a number if the input is invalid
        while (not 1 <= user_choice <= len(available_formats)):
            user_choice = int(input("Please enter a listed number: "))

        # Matches the user choice to its format
        output_format = available_formats[user_choice - 1]
        print(f"{output_format} selected")

        # Creates a file name using the old file name and new format
        output_file = os.path.splitext(input_file)[0] + '.' + output_format.lower()

        # Saves the image
        img.save(output_file, output_format)
        print(f"{input_file} saved as {output_format}!")

except IOError:
    print("Error: Invalid image file.")