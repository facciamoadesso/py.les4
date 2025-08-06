from PIL import Image
image = Image.open("lenna.jpg")
rgb_image = image.convert("RGB")
print("rgb_image.mode")

rgb_image = rgb_image.resize((1200, 630))

print(rgb_image.width)
print(rgb_image.height)
print(rgb_image.mode)