"""Module for saving qoutes in a class."""


class QuoteModel:
    """Data Model for the qoutes."""

    def __init__(self, body, author):
        """Quotemodel initialization."""
        self.body = body
        self.author = author

