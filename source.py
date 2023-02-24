import os
import codecs


from bs4 import BeautifulSoup
from googletrans import Translator
from html.parser import HTMLParser


script_path = os.getcwd()


###
# open the file and returns its content as a string
###
def open_file(file_name: str):
    folder_path = script_path + r"\Targeted_Website" + f"\{file_name}"
    file_handle = codecs.open(folder_path, 'r', "utf-8")
    file_content = file_handle.read()
    file_handle.close()

    return file_content


def translate_sentence(text: str):
    translator = Translator()
    result = translator.translate(text, dest="de", src="en")
    return result.text



def write_file(text: str, file_name: str):
    folder_path = script_path + r"\Translated_Website" + f"\{file_name}"
    file_handle = codecs.open(folder_path, "w", "utf-8")
    file_handle.write(text)
    file_handle.close()


##################################################################################################
# running sequence
def main():
    file_content = open_file("about.html")

    print(file_content)

    # new_translated_content = translate_sentence(file_content)

    write_file(file_content, "translated.html")



##################################################################################################
# run
if __name__ == "__main__":
    main()