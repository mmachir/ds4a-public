
import pandas as pd
import requests
import os.path
import json
import re


def validate_input():
    while True:
        # get input
        file = input("Text file to translate to lolspeak: ")
        # validate file type (.txt)
        if not file.endswith('.txt'):
            print("Make sure this is a text file. The file extension should be '.txt'. Please try again.")
            continue
        # validate file path
        elif not os.path.isfile(file):
            print("The file was not found. Please verify your file path and try again.") 
            continue
        else:
            # file input validated
            return file

def get_lol_dictionary():
    url = "https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json"
    resp = requests.get(url)
    data = json.loads(resp.text)
    return data

def main():
    # get input file
    input_file = validate_input()
    # set up output file
    output_file = input_file.split('.txt')[0]+'_lolcat.txt'
    # access lol dictionary
    data = get_lol_dictionary()
    # read in text from file
    with open(input_file, "r",errors="replace") as f1, open(output_file, "w",errors="replace") as f2:
        textdoc = f1.readlines()
        # iterate through each line
        for textstr in textdoc:
            # convert line to list of words
            wordlist = textstr.split(' ')
            lollist = []
            # iterate through each word
            for word in wordlist:
                # searchterm = word minus any special characters at the end
                searchterm = re.sub(r'([^\w\s]|_)+(?=\s|$)', '', word).lower()
                # remove any line breaks
                searchterm = re.sub(r'[\r\n]+','', searchterm)
                # look for searchterm in lol dictionary
                if searchterm in data:
                    # replace the original word but keep any of the special chars/line breaks
                    word = data[searchterm] + word[len(searchterm):]
                # add the dictionary translation or original word back to new list
                lollist.append(word)
            # compose lolstring, dropping any words replaced by '' in the lol translation
            lolstring = ' '.join([word for word in lollist if word])
            # write the translated line to output file
            f2.write(lolstring)
    print(f'Translation complete! New file: {output_file}')

if(__name__ == '__main__'):
    main()
