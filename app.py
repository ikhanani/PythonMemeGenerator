import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeEngine.MemeEngine import MemeEngine
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for f in os.listdir(images_path):
        if f.endswith(".jpg"):
            imgs.append(os.path.join(images_path, f))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.quote, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    url = request.form['image_url']
    pic = requests.get(url)
    with open("./tmp.jpg", "wb") as f:
        f.write(pic.content)
    try:
        img = Image.open("./tmp.jpg")
    except Exception:
        return render_template('invalid_image.html')
    path = meme.make_meme("./tmp.jpg",
                          request.form['body'], request.form['author'])
    os.remove("./tmp.jpg")

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
