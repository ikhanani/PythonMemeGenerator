from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from typing import List
from QuoteEngine.TextIngestor import TextIngestor
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return (path.find('.pdf') != -1 or path.find('.txt') != -1
                or path.find('.csv') != -1 or path.find('.docx') != -1)

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if(cls.can_ingest(path)):
            if(path.find('.txt') != -1):
                t = TextIngestor()
                return t.parse(path)
            elif(path.find('.csv') != -1):
                c = CSVIngestor()
                return c.parse(path)
            elif(path.find('.pdf') != -1):
                p = PDFIngestor()
                return p.parse(path)
            else:
                d = DocxIngestor()
                return d.parse(path)
