from PIL import Image  # Ask for the artisan's specific skill

# Open an image file
image = Image.open('path_to_your_image.jpg')

# The artisan works their magic: rotate and convert to grayscale
rotated_image = image.rotate(45)
bw_image = rotated_image.convert('L')

# Save the new creation
bw_image.save('my_artistic_image.jpg')