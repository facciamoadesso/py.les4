from PIL import Image

green = Image.open("green_channel.jpg")
coordinates = (25, 0, 620, 522)
cropped = green.crop(coordinates)
cropped.save("cropped_green.jpg")
print("cropped_green.jpg")
print("Size:", cropped.size)