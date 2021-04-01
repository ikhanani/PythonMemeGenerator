# Meme Generator
This application generates a meme from either user supplied text and images. If nothing is given as input, a random meme will be generated. Memes can be created both from the command line and the Flask application.

## Dependencies
All dependencies can be installed by running ```pip install -r requirements.txt```
## Running from meme.py
To run this program from the command line, run ```python3 meme.py```. Optionally, the following arguments can be used to supply the image, quote, and author.

```--body```: The main quote of the meme
```--author```: Author of the quote
```--path```: Path to image

## Running from app.py (webpage)

Run the program with ```python3 app.py```. This will start up the server and you can navigate to the webpage at http://127.0.0.1:5000/. There, you have the option to either create a random meme or your own custom meme.

## Design

The project utilizes multiple Ingestor classes to read various file types into QuoteModel objects which have a quote and an author. The MemeEngine manages the act of creating the meme from the given text and image.

#### Ingestors

###### IngestorInterface

The base class from which all other ingestors are created from. Has two methods, can_ingest and parse, which the other ingestors will implement.

###### TextIngestor

Parses .txt files and returns a list of QuoteModels.

###### DocxIngestor

Parses .docx files using the ```python-docx``` library and returns a list of QuoteModels.

###### CSVIngestor

Parses .csv files using the ```pandas``` library and returns a list of QuoteModels.

###### PDFIngestor

Parses .pdf files using a ```pdftotext``` subprocess and returns a list of QuoteModels.

#### MemeEngine

Takes in an image, quote, and author. Creates the specified meme and returns the path to the final image with the ```make_meme``` method.