"""meme generator command line app."""
import os
import random
import argparse


from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None
    allowed_images = ["jpg", "jpeg", "png"]
    if path is None:
        images_path = "./_data/photos/dog/"
        imgs = []
        for file in os.listdir(images_path):
            ext = file.split(".")[-1]
            if ext in allowed_images:
                imgs.append(f"{images_path}{file}")

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv",
        ]
        quotes = []
        for f in quote_files:
            quotes += Ingestor.parse(f)

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine("./generated_memes")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate a Meme")
    parser.add_argument("--path", type=str, help="path to an image file")
    parser.add_argument("--body", type=str, help="quote body to add to the image")
    parser.add_argument("--author", type=str, help="quote author to add to the image")
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
