"""Interface for all the ingestors modules."""
from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Interface for all the ingestor classes."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Take a file path and return whether can be ingested or not."""
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take a file path as input and returns list of QuoteModel objects."""
        pass
