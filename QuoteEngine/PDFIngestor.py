from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from typing import List
import subprocess
import random
import os


class PDFIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """ Determine if the supplied path can be parsed """
        return path.find('.pdf') != -1

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse PDF file and return list of QuoteModel objects """
        if(cls.can_ingest(path)):
            tmp = f'{random.randint(0,1000000)}.txt'
            call = subprocess.call(['pdftotext', path, tmp])
            file_ref = open(tmp, "r", encoding="utf-8-sig")
            result = []
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split('-')
                    result.append(QuoteModel(parsed[1].strip(),
                                  parsed[0].strip()))

            file_ref.close()
            os.remove(tmp)

            return result
        else:
            raise Exception("Cannot parse file, incorrect type")
