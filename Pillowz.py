from PIL import Image  # Ask for the artisan's specific skill
from PIL import ImageFilter

# Open an image file
image = Image.open('pexels-pixabay-265072.jpg')

# The artisan works their magic: rotate and convert to grayscale
rotated_image = image.rotate(45)
bw_image = rotated_image.convert('L')

# Save the new creation
bw_image.save('my_artistic_image.jpg')

#filter the image
filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save('my_filtered_image.jpg')

#blur the image
blurred_image = image.filter(ImageFilter.GaussianBlur(5))
blurred_image.save('my_blurred_image.jpg')

