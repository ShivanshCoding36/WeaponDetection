print("Started")
import os
from PIL import Image
print('Library Imported')
def resize_and_convert_to_grayscale(image_path, size=(250, 250)):
    try:
        # Open an image file
        with Image.open(image_path) as img:
            # Resize the image
            img = img.resize(size)
            # Convert the image to grayscale
            gray_img = img.convert('L')
            # Save the grayscale image
            gray_img.save(image_path)
            print(f"Image {image_path} has been resized and converted to grayscale.")
    except IOError:
        print(f"Unable to open image {image_path}. Skipping.")

def process_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename:
            image_path = os.path.join(folder_path, filename)
            resize_and_convert_to_grayscale(image_path)

# Replace 'path_to_your_folder' with the path to the folder containing your images
print("Begining Process")
process_images_in_folder('Pistol')
print("Done")
process_images_in_folder('Knife')
print("Done")
process_images_in_folder('eval_pistol')
print("Done")
process_images_in_folder('eval_Knife')
print("Done")