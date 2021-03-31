from abc import ABC, abstractmethod 
from typing import List

from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    @classmethod
    def can_ingest(cls, path) -> bool:
        pass

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass