# Reviving beatles
This projects is to build new letters songs based on many letters of specific artists, which are get by scraping and save on *.txt* files. For build a new letter from the zero, all preprocessed text files are given as input to the LSTM model to train your predction and, to construct a new one, just given a title to the song and, with this title, the model will predict new characters based on what he has already built.

## Scraping

The main file <a href="https://github.com/AntonioNvs/reviving-beatles/blob/main/scraping.py" target="_blank">scraping.py</a> do the scraping of all letters of a specifc artist given as parameter, along with the link to <a href="https://www.letras.com/" target="_blank"> Letras.com </a>, where is made the scraping.
