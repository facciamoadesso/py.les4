from PIL import Image

red = Image.open("red_channel.jpg")
green = Image.open("green_channel.jpg")
blue = Image.open("blue_channel.jpg")

merged_image = Image.merge("RGB", (red, green, blue))
merged_image.save("merged_photo.jpg")
print("merged_photo.jpg")