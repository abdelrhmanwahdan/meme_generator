"""Module for ingesting docx files."""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Ingest each line in docx files and transform it into a QuoteModel class."""

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take a file path as input and returns list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        qoutes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split("-")
                new_qoute = QuoteModel(parse[0], parse[1])
                qoutes.append(new_qoute)

        return qoutes
