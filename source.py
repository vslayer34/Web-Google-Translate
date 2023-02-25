import os
import codecs
import re


from bs4 import BeautifulSoup
from googletrans import Translator
from html.parser import HTMLParser


# re = <.*?>



script_path = os.getcwd()


to_translat = {}


###
# add the paragraph and the the translated paragraph to the dictionary
###
def add_to_dict(sentence: str, translated_sentence: str):
    to_translat[sentence] = translated_sentence



###
# Check sentence to get the paragraphs ignoring the tags
###
def check_sentence(sentence: str):    

    pattern = "<.*?>"
    new_line = re.sub(pattern, "", sentence, 1000)

    return new_line

###
# open the file and returns its content as a string
###
def open_file(file_name: str):
    # get the targeted folder path
    folder_path = script_path + r"\Targeted_Website" + f"\{file_name}"
    # open the file
    # use of codecs to make python read and parse html files
    file_handle = codecs.open(folder_path, 'r', "utf-8")
    
    # go through each line
    for line in file_handle.readlines():

        new_line = check_sentence(line)

        if new_line.strip() != "":
            # translate the extracted paragraph
            translated_line = translate_sentence(new_line)
            # add it to a dict containing every paragraph and its translated equaflent
            add_to_dict(new_line, translated_line)
            
        # write a new file
        write_file(line, file_name, new_line)

    file_handle.close()


###
# take the sentence that should be translated
###
def translate_sentence(text: str):
    print(text)
    translator = Translator()
    result = translator.translate(text, dest="hi", src="en")
    return result.text



###
# Write the new file
# and apply the translation to it
###
def write_file(text: str, file_name: str, text_to_be_replaced):
    # path to the newly created file
    folder_path = script_path + r"\Translated_Website" + f"\{file_name}"
    file_handle = codecs.open(folder_path, "a+", "utf-8")
    # replace the original text with the translated one
    translated_text = apply_translation(text, text_to_be_replaced)
    file_handle.write(translated_text)
    file_handle.close()


###
# search the dictionary
# and replace the paragraphs with the translated text
###
def apply_translation(text: str, text_to_be_replaced):
    for key in to_translat.keys():
        # compare the texts and replace it
        if key.strip() == text_to_be_replaced.strip():
            new_text = text.replace(text_to_be_replaced.strip(), to_translat[key])
            return new_text
    return text


##################################################################################################
# running sequence
def main():
    open_file("index.htm")


##################################################################################################
# run
if __name__ == "__main__":
    main()