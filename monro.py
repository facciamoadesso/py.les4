from PIL import Image

image = Image.open("monro.jpg")
rgb_image = image.convert("RGB")
red, green, blue = rgb_image.split()
red.save("red_channel.jpg")
green.save("green_channel.jpg")
blue.save("blue_channel.jpg")

print("red_channel.jpg")
print("green_channel.jpg")
print("blue_channel.jpg")
