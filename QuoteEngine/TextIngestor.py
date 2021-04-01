from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from typing import List


class TextIngestor(IngestorInterface):
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """ Determine if the supplied path can be parsed """
        return path.find('.txt') != -1

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse txt file and return list of QuoteModel objects """
        if(cls.can_ingest(path)):
            result = []
            f = open(path, "r", encoding="utf-8-sig")
            for line in f:
                q, a = line.split("-")
                result.append(QuoteModel(a.strip(), q.strip()))
            return result
        else:
            raise Exception("Cannot parse file, incorrect type")
