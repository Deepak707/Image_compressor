import os
import sys

from PIL import Image

def compress_image(image_path, output_path, quality):
    with Image.open(image_path) as img:
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        img.save(output_path, "JPEG", optimize=True, quality=quality)

def process_images(input_folder, output_folder, quality):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_types = ('.jpg', '.jpeg', '.png')

    for file_type in file_types:
        all_images = [f for f in os.listdir(input_folder) if f.endswith(file_type)]

        for image in all_images:
            input_path = os.path.join(input_folder, image)
            output_path = os.path.join(output_folder, image)

            compress_image(input_path, output_path, quality)

if __name__ == "__main__":
    input_folder = input("Enter the path of the images folder: ")
    output_folder = input("Enter the path of the output folder: ")
    quality = int(input("Enter the desired quality (70-80): "))

    if quality < 70 or quality > 80:
        print("Quality should be between 70 and 80.")
        sys.exit(1)

    process_images(input_folder, output_folder, quality)
    print("Image compression completed.")