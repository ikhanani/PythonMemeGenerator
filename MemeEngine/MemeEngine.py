from PIL import Image, ImageDraw, ImageFont
import os
import random


class MemeEngine:

    def __init__(self, dir):
        """ Create MemeEngine and set base directory """
        self.dir = dir

        if not os.path.exists(dir):
            os.makedirs(dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """ Create meme from supplied image, text, and author and return the path to the final image """
        try:
            out = self.dir + '/' + f'{random.randint(0,1000000)}.jpg'
            img = Image.open(img_path)
            if width > 500:
                width = 500
            height = width * img.height / img.width
            img = img.resize((int(width), int(height)))
            result = ImageDraw.Draw(img)
            result.text((random.randint(50, int(width)-200), random.randint(50, int(height)-200)),
                        text.replace('’', '\'') + "\n - " + author)
            img.save(out, "JPEG")
            return(out)
        except Exception as e:
            raise Exception("Error generating meme:", e)
