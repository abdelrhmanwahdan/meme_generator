# Meme Generator

This project is a web app meme generator that takes a bunch of quotes from their authors and prints them on different images in random places on the images you can add photos by adding your photos to the photos/dog folder. You can get your quotes in the following formats: PDF, txt, CSV, or Docx the project will ingest any of these file types.

## Requirments

- Create a virtual environment using the command `python3 -m venv ./venv` in the current directory
- Activate the virtual environment using the command `source ./venv/bin/activate`
- Install the packages in the `requirments.txt` file using the following command:
  `pip install -r (full path of the requirments.txt file)`
- Download the [pdftotext](https://www.xpdfreader.com/download.html) command line tool.

## Run

you have two options to run this project:

- you can either run it from the command line by running `meme.py` and it will generate a random meme in the `generated_memes` folder or you can specify the optional parameters you can add `--path (the image path)`, `--body (body of the qoute)` and `--author (author of the qoute)`
- Or you can run the project as a web app by running the command:`flask run`
  and the project will run on the server https://localhost:5000 .

## Sub-modules

- Flask: a Web micro framework we use it to run the project on a web server
- subprocess: this module is used to interact with other command line tools inside python

## Acknowledgments

This project is part of the [Intermediate python nanodegree](https://www.udacity.com/course/intermediate-python-nanodegree--nd303) of [Udacity](https://www.udacity.com/).
