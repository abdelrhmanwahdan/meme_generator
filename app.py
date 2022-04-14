"""Meme generator flask web app."""

import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel


app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """Load all resources."""
    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    # quote_files variable
    quotes = []
    for file in quote_files:
        quotes += Ingestor.parse(file)

    images_path = "./_data/photos/dog/"

    allowed_images = ["jpg", "jpeg", "png"]
    imgs = []
    for file in os.listdir(images_path):
        ext = file.split(".")[-1]
        if ext in allowed_images:
            imgs.append(f"{images_path}{file}")

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get("image_url")
    if not image_url:
        return render_template("meme_form.html")
    try:
        image_data = requests.get(image_url, stream=True).content
        image = "./temp.jpeg"
        with open(image, "wb") as file:
            file.write(image_data)
        qoute = request.form.get("body")
        author = request.form.get("author")
        path = meme.make_meme(image, qoute, author)
        return render_template("meme.html", path=path)

    except Exception as e:
        print(e)
        return render_template("meme_form.html")


if __name__ == "__main__":
    app.run()
