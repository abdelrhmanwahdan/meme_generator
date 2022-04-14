"""Module for ingesting txt files."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """Ingest each line in txt files and transform it into a QuoteModel class."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take a file path as input and returns list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("Cannot Ingest Exception")

        qoutes = []
        with open(path, "r") as f:

            for line in f.readlines():
                line = line.strip("\n\r").strip()
                if len(line) > 0:
                    parsed = line.split("-")
                    new_qoute = QuoteModel(parsed[0], parsed[1])
                    qoutes.append(new_qoute)

        return qoutes
