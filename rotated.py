from PIL import Image

image = Image.open("example.jpg")
rotated_image = image.rotate(45)
rotated_image.save("rotated.jpg")

image.thumbnail((600, 1200))

print("Width:", image.width)
print("Height:", image.height)
print("Original colour model:", image.mode)
cmyk_image = image.convert("CMYK")
print("Converted colour model", cmyk_image.mode)
