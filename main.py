from PIL import Image
import os

input_file = ["image.jpeg", "image2.jpeg", "image3.jpeg"]
available_formats = ['PNG', 'JPEG', 'PDF', 'WEBP']
list_counter = 0
user_choice = 0

for file in input_file:
    try:
        with Image.open(input_file[list_counter]) as img:
            print("Valid image file.")
            list_counter += 1
    except IOError:
        raise Exception("Error: Invalid image file.")

print(f"What format do you want to convert {input_file} to?")

for i, formats, in enumerate(available_formats):
    print(f"{i + 1}. {formats} ")

user_choice = int(input("Enter a number: "))

while not 1 <= user_choice <= len(available_formats):
    user_choice = int(input("Please enter a listed number: "))

output_format = available_formats[user_choice - 1]
print(f"{output_format} selected")

list_counter = 0
user_choice = 0
images = [Image.open(filename) for filename in input_file]

if output_format == 'PDF':
    print("Do you want your files appended?\n1. Yes\n2. No")

    user_choice = int(input("Enter a number: "))

    while not 1 <= user_choice <= 2:
        user_choice = int(input("Please enter a listed number: "))

    if user_choice == 1:
        output_file = os.path.splitext(input_file[list_counter])[0] + '.' + output_format.lower()
        images[list_counter].save(output_file, output_format, save_all=True, append_images=images[1:])

    elif user_choice == 2:
        for i in input_file:
            output_file = os.path.splitext(input_file[list_counter])[0] + '.' + output_format.lower()
            images[list_counter].save(output_file, output_format)
            list_counter += 1

elif output_format == 'GIF':
    print("GIF")
else:
    print("PDF/JPEG/WEBP")
    for i in input_file:
        output_file = os.path.splitext(input_file[list_counter])[0] + '.' + output_format.lower()
        images[list_counter].save(output_file, output_format)
        list_counter += 1