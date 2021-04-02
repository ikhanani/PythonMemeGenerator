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
            font = ImageFont.truetype('Arial.ttf', 20)
            result = ImageDraw.Draw(img)
            textx = random.randint(50, int(width)-200)
            text = text.replace('’', '\'')
            result.text((textx, random.randint(50, int(height)-200)),
                        self.wrap_text(text, font, textx, width) + "\n - " + author, font=font)
            img.save(out, "JPEG")
            return(out)
        except Exception as e:
            raise Exception("Error generating meme:", e)

    def wrap_text(self, text, font, textx, width):
        if(font.getsize(text)[0] <= width - textx - 10):
            return text
        result = ''
        words = text.split(' ')
        count = 0
        while count < len(words):
            tmp = ''
            while(count < len(words) and font.getsize(tmp + words[count])[0] <= width - textx - 10):
                tmp = tmp + ' ' + words[count]
                count += 1
            result = result + tmp + '\n'
        return result


