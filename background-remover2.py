import os
from rembg import remove
from PIL import Image


def remove_background(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    image_files = [f for f in os.listdir(input_directory) if f.endswith((".png", ".jpg", ".jpeg"))]

    for image_file in image_files:
        input_path = os.path.join(input_directory, image_file)
        output_path = os.path.join(output_directory, image_file)

        with open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
            img_data = f_in.read()
            output_data = remove(img_data)
            f_out.write(output_data)

        print(f"Background removed for image file: {output_path}")


input_directory = 'D:/git/thesis/background-remover/input'
output_directory = 'D:/git/thesis/background-remover/output'
remove_background(input_directory, output_directory)
