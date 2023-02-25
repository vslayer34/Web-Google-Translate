import os
import codecs
import re


from bs4 import BeautifulSoup
from googletrans import Translator
from html.parser import HTMLParser


# re = <.*?>



script_path = os.getcwd()


to_translat = {}

def add_to_dict(sentence: str, translated_sentence: str):
    to_translat[sentence] = translated_sentence
    # to_translat.update({sentence: translate_sentence})
    print(to_translat)



###
# Check sentence to get the paragraphs
###
def check_sentence(sentence: str):    

    pattern = "<.*?>"
    new_line = re.sub(pattern, "", sentence, 1000)

    return new_line

###
# open the file and returns its content as a string
###
def open_file(file_name: str):
    folder_path = script_path + r"\Targeted_Website" + f"\{file_name}"
    file_handle = codecs.open(folder_path, 'r', "utf-8")
    
    for line in file_handle.readlines():
        
        print(line)
        new_line = check_sentence(line)
        # print("XXXXXXXXXX")
        print(new_line)
        if new_line.strip() != "":
            translated_line = translate_sentence(new_line)
            add_to_dict(new_line, translated_line)
            
        write_file(line, file_name)

    file_handle.close()

    # return file_content


def translate_sentence(text: str):
    print(text)
    translator = Translator()
    result = translator.translate(text, dest="de", src="en")
    return result.text



def write_file(text: str, file_name: str):
    folder_path = script_path + r"\Translated_Website" + f"\{file_name}"
    file_handle = codecs.open(folder_path, "a+", "utf-8")
    file_handle.write(text)
    file_handle.close()


##################################################################################################
# running sequence
def main():
    file_content = open_file("about.html")

    # print(file_content)

    # new_translated_content = translate_sentence(file_content)

    # write_file(file_content, "translated.html")



##################################################################################################
# run
if __name__ == "__main__":
    main()