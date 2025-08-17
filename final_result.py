from PIL import Image

red = Image.open("red_channel.jpg")
red_left = red.crop((50, 0, red.width, red.height))
red_middle = red.crop((25, 0, red.width - 25, red.height))
blended_red = Image.blend(red_left, red_middle, 0.5).crop((0, 0, 595, 522))

blue = Image.open("blue_channel.jpg")
blue_right = blue.crop((0, 0, blue.width-50, blue.height))
blue_middle = blue.crop((25, 0, blue.width - 25, blue.height))
blended_blue = Image.blend(blue_right, blue_middle, 0.5).crop((0, 0, 595, 522))

green = Image.open("green_channel.jpg").crop((25, 0, 620, 522))

final_merged = Image.merge("RGB", (blended_red, green, blended_blue))
final_merged.save("merged_channels.jpg")

avatar = Image.open("merged_channels.jpg")
avatar.thumbnail((80, 80))
avatar.save("avatar.jpg")
