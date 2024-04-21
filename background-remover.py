from rembg import remove
from PIL import Image

# Open the input image
input_image = Image.open('D:/git/thesis/background-remover/data sets/test.jpg')

# Remove the background
output_image = remove(input_image)

# Save the output image
output_image.save('output_image.png')