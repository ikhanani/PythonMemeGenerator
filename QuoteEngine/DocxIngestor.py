from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from typing import List
import docx


class DocxIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """ Determine if the supplied path can be parsed """
        return path.find('.docx') != -1

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse docx file and return list of QuoteModel objects """
        if(cls.can_ingest(path)):
            result = []
            f = docx.Document(path)
            for line in f.paragraphs:
                if line.text != "":
                    meme = line.text.split("-")
                    result.append(QuoteModel(meme[1].strip(), meme[0].strip()))
            return result
        else:
            raise Exception("Cannot parse file, incorrect type")
