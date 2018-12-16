import html2text
import os
import codecs
import io
import chardet

filenames = []

def get_data_from_file(pathAndFileName):
    with io.open(pathAndFileName, 'r', encoding = "ISO-8859-1") as theFile:
        data = theFile.read()
        return data

def prepare_arff_file():
    with io.open('result.arff', 'a', encoding='utf-8') as file:
        file.write('@relation dokumenty\n@attribute tytul string\n@attribute zawartosc string\n@data\n')

def add_dir_to_arff_file(path):
    for filename in os.listdir(path):
        html = get_data_from_file(path + filename)
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        text = h.handle(html)
        text = clear_text(text)
        if filename in filenames:
            filename = filename + '0'
        with io.open('result.arff', 'a', encoding='utf-8') as file:
            file.write('"' + filename + '","' + text + '"' + '\n')
        filenames.append(filename)

def clear_text(text):
    text = text.replace("\n", " ")
    text = text.replace("\\r\\n", " ")
    text = text.replace("\\r", " ")
    text = text.replace("\"", " ")
    text = text.replace("?", " ")
    text = text.replace("!", " ")
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    text = text.replace("|", " ")
    text = text.replace("`", " ")
    text = text.replace("'", " ")
    text = text.replace("’", " ")
    text = text.replace("‘", " ")
    text = text.replace("*", " ")
    text = text.replace("#", " ")
    text = text.replace(":", " ")
    text = text.replace(";", " ")
    text = text.replace("\"", " ")
    text = text.replace("-", " ")
    text = text.replace("–", " ")
    text = text.replace("+", " ")
    text = text.replace("=", " ")
    text = text.replace("[", " ")
    text = text.replace("]", " ")
    text = text.replace(")", " ")
    text = text.replace(")", " ")
    text = text.replace("@", " ")
    text = text.replace("$", " ")
    text = text.replace("%", " ")
    text = text.replace("&", " ")
    text = text.replace("…", " ")
    text = text.replace("/", " ")
    text = text.replace("\\", " ")
    text = text.replace("_", " ")
    text = " ".join(text.split())
    return text

prepare_arff_file()
add_dir_to_arff_file("C:/Users/Monika/Downloads/websphinx-example/course/")
add_dir_to_arff_file("C:/Users/Monika/Downloads/websphinx-example/mod/data/")
add_dir_to_arff_file("C:/Users/Monika/Downloads/websphinx-example/mod/page/")

 