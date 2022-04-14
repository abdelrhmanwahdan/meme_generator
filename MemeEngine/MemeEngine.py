"""Engine for generating different memes with different tools."""
from PIL import Image, ImageDraw, ImageFont
import random

import textwrap


class MemeEngine:
    """An engine to generate different memes using images and qoutes."""

    def __init__(self, output_dir):
        """Init file for the Meme engine class."""
        self.output_dir = output_dir
        self.allowed_images = ["jpg", "jpeg", "png"]

    def can_ingest(self, path):
        """Take an image path and return whether can be ingested or not."""
        ext = path.split(".")[-1]
        return ext in self.allowed_images

    def make_meme(self, img_path, text, author) -> str:
        """Return a meme by taking image path, text to write on the image and author of the text.

        arguments:
        img_path: the path of the image
        text: text to write on the image
        author: author of the text

        retrurns:
        path: path of the saved image
        """
        if not self.can_ingest(img_path):
            raise Exception("Cannot Ingest Exception")

        maxwidth = 500
        img = Image.open(img_path)
        img_width, img_height = img.size

        if img_width > maxwidth:
            width_percent = maxwidth / float(img_width)
            height_size = int((float(img_height) * float(width_percent)))
            img = img.resize((maxwidth, height_size), Image.ANTIALIAS)
            img_width, img_height = img.size

        img_draw = ImageDraw.Draw(img)
        random_place = (
            20,
            random.randint(20, img_height - 50),
        )
        font = ImageFont.truetype("./_data/Fonts/arial.ttf", 20)

        # Wrap the qoute body.
        wrapper = textwrap.TextWrapper(width=50)
        string = wrapper.fill(text=text)

        full_qoute = f"{string}\n{author}"
        img_draw.text(random_place, full_qoute, fill=(255, 0, 0), font=font)
        img_name = f"{random.randint(0,10000000000)}.jpg"
        path = f"{self.output_dir}/{img_name}"
        img.save(path)

        return path
