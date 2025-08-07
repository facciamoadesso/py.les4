from PIL import Image

image = Image.open("monro.jpg")
rgb_image = image.convert("RGB")
red, green, blue = rgb_image.split()

red.save("red_channel.jpg")
green.save("green_channel.jpg")
blue.save("blue_channel.jpg")

merged_image = Image.merge("RGB", (red, green, blue))
merged_image.save("merged_photo.jpg")

red = Image.open("red_channel.jpg")
red_left = red.crop((50, 0, red.width, red.height))
red_middle = red.crop((25, 0, red.width - 25, red.height))
blended_red = Image.blend(red_left, red_middle, 0.5)
final_red = blended_red.crop((0, 0, 595, 522))
final_red.save("shifted_red.jpg")

blue = Image.open("blue_channel.jpg")
blue_right = blue.crop((50, 0, blue.width, blue.height))
blue_middle = blue.crop((25, 0, blue.width - 25, blue.height))
blended_blue = Image.blend(blue_right, blue_middle, 0.5)
final_blue = blended_blue.crop((0, 0, 595, 522))
final_blue.save("shifted_blue.jpg")

green = Image.open("green_channel.jpg")
cropped_green = green.crop((25, 0, 620, 522))
cropped_green.save("cropped_green.jpg")

red = Image.open("shifted_red.jpg")
green = Image.open("cropped_green.jpg")
blue = Image.open("shifted_blue.jpg")
final_merged = Image.merge("RGB", (red, green, blue))
final_merged.save("merged_channels.jpg")

avatar = Image.open("merged_channels.jpg")
avatar.thumbnail((80, 80))
avatar.save("avatar.jpg")