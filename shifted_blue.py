from PIL import Image

image = Image.open("blue_channel.jpg")
blue_right = image.crop((50, 0, image.width, image.height))
blue_middle = image.crop((25, 0, image.width - 25, image.height))
blended = Image.blend(blue_right, blue_middle, 0.5)
final_blue = blended.crop((0, 0, 595, 522))
final_blue.save("shifted_blue.jpg")
print("Final blue size:", final_blue.size)