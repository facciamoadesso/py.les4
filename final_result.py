from PIL import Image

original = Image.open("monro.jpg")
red, green, blue = original.split()

def blend_from_two_crops(channel, crop1, crop2):
    return Image.blend(
        channel.crop(crop1),
        channel.crop(crop2),
        0.5
    ).crop((0, 0, 595, 522))

blended_red = blend_from_two_crops(
    red,
    (50, 0, red.width, red.height),
    (25, 0, red.width - 25, red.height)
)

blended_blue = blend_from_two_crops(
    blue,
    (0, 0, blue.width - 50, blue.height),
    (25, 0, blue.width - 25, blue.height)
)

cropped_green = green.crop((25, 0, 620, 522))

final_merged = Image.merge("RGB", (blended_red, cropped_green, blended_blue))
final_merged.save("merged_channels.jpg")

avatar = final_merged.copy()
avatar.thumbnail((80, 80))
avatar.save("avatar.jpg")


