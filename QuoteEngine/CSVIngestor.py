from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from typing import List
import pandas


class CSVIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """ Determine if the supplied path can be parsed """
        return path.find('.csv') != -1

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse CSV file and return list of QuoteModel objects """
        if(cls.can_ingest(path)):
            result = []
            df = pandas.read_csv(path, header=0)
            for index, row in df.iterrows():
                result.append(QuoteModel(row['author']
                              .strip(), row['body'].strip()))
            return result
        else:
            raise Exception("Cannot parse file, incorrect type")
