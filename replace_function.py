from PIL import Image

def replace(image, old_color, new_color):
    """
    A function that replaces one color of an image with another one

    image : str
        a string refering to the images file path

    old_color : tuple
        the target color to replace

    new_color : tuple
        the new color to set the pixels to
    """
    # open image
    rgb_image = Image.open(image).convert("RGB")
    # run through all pixels
    for x in range(rgb_image.width):
        for y in range(rgb_image.height):
            pixel = rgb_image.getpixel((x,y))
            # replace all pixel colors
            if pixel == old_color:
                rgb_image.putpixel((x,y), new_color)
    # return new image
    return rgb_image
