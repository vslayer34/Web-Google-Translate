import os
from googletrans import Translator

script_path = os.getcwd()


###
# open the file and returns its content
###
def open_file(file_name: str):
    folder_path = script_path + r"\test files" + f"\{file_name}"
    file_handle = open(folder_path)
    file_content = file_handle.read()
    file_handle.close()

    return file_content


def translate_sentence(text: str):
    translator = Translator()
    result = translator.translate(text, dest="de", src="en")
    return result.text



def write_file(text: str, file_name: str):
    folder_path = script_path + r"\test files" + f"\{file_name}"
    file_handle = open(folder_path, "w")
    file_handle.write(text)
    file_handle.close()


##################################################################################################
# running sequence
def main():
    file_content = open_file("test.txt")

    new_translated_content = translate_sentence(file_content)

    write_file(new_translated_content, "translated.txt")



##################################################################################################
# run
if __name__ == "__main__":
    main()