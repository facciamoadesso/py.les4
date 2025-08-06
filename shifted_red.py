from PIL import Image

image = Image.open("red_channel.jpg")
red_left = image.crop((50, 0, image.width, image.height))
red_middle = image.crop((25, 0, image.width - 25, image.height))
blended = Image.blend(red_left, red_middle, 0.5)

final_red = blended.crop((0, 0, 595, 522))
final_red.save("shifted_red.jpg")
print("Final red size:", final_red.size)