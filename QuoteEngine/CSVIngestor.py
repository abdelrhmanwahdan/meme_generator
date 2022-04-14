"""Module for ingesting CSV files."""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Ingest each line in CSV files and transform it into a QuoteModel class."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take a file path as input and returns list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        qoutes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_qoute = QuoteModel(row["body"], row["author"])
            qoutes.append(new_qoute)

        return qoutes
