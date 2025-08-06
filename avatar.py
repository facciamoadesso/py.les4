from PIL import Image

image = Image.open("merged_channels.jpg")
print("Original size:", image.size)
image.thumbnail((80, 80))
print("Thumbnail size:", image.size)
image.save("avatar.jpg")
print("avatar.jpg")