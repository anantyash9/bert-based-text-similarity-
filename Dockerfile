from python:3.6
copy text_similarity.py /app/text_similarity.py
copy importer.py /app/importer.py
workdir /app
run pip install semantic-text-similarity flask flask-cors
run python importer.py
cmd python text_similarity.py