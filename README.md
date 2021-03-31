# Meme Generator
This application generates a meme from either user supplied text and images. If nothing is given as input, a random meme will be generated.
## Running from meme.py
To run this program from the command line, run ```python3 meme.py```. Optionally, the following arguments can be used to supply the image, quote, and author.

```--body```: The main quote of the meme
```--author```: Author of the quote
```--path```: Path to image

## Running from app.py (webpage)

Run the program with ```python3 app.py```. This will start up the server and you can navigate to the webpage at http://127.0.0.1:5000/. There, you have the option to either create a random meme or your own custom meme.

## Design

The project utilizes multiple Ingestor classes to read various file types into QuoteModel objects which have a quote and an author. The MemeEngine manages the act of creating the meme from the given text and image.