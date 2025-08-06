from PIL import Image

red = Image.open("shifted_red.jpg")
green = Image.open("cropped_green.jpg")
blue = Image.open("shifted_blue.jpg")
merged = Image.merge("RGB", (red, green, blue))
merged.save("merged_channels.jpg")
print("merged_channels.jpg")