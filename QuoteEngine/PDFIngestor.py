"""Module for ingesting pdf files."""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Ingest each line in PDF files and transform it into a QuoteModel class."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take a file path as input and returns list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("Cannot Ingest Exception")

        tmp = f"{random.randint(0, 1000000)}.txt"
        subprocess.run(["pdftotext", path, tmp])
        qoutes = []
        with open(tmp) as f:

            for line in f.readlines():
                line = line.strip("\n\r").strip()
                if len(line) > 0:
                    parsed = line.split("-")
                    new_qoute = QuoteModel(parsed[0], parsed[1])
                    qoutes.append(new_qoute)

        os.remove(tmp)
        return qoutes
