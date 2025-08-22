from PIL import Image

original = Image.open("monro.jpg")

red, green, blue = original.split()

blended_red = Image.blend(
    red.crop((50, 0, red.width, red.height)),
    red.crop((25, 0, red.width - 25, red.height)),
    0.5
)

blended_blue = Image.blend(
    blue.crop((0, 0, blue.width - 50, blue.height)),
    blue.crop((25, 0, blue.width - 25, blue.height)),
    0.5
)

cropped_green = green.crop((25, 0, green.width - 25, green.height))

final_merged = Image.merge("RGB", (blended_red, cropped_green, blended_blue))
final_merged.save("merged_channels.jpg")

avatar = final_merged.copy()
avatar.thumbnail((80, 80))
avatar.save("avatar.jpg")
