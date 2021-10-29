#!/usr/bin/env python
# coding: utf-8

import spacy
from bs4 import BeautifulSoup
import json
import re
from nltk.tokenize import wordpunct_tokenize, word_tokenize

# with open('datasets/foodbase/FoodBase_curated.xml', 'r') as f:
#     data = f.read()
with open('datasets/foodbase/FoodBase_uncurated.xml', 'r') as f:
    data = f.read()

Bs_data = BeautifulSoup(data, "xml")

b_doc = Bs_data.find_all('document')

print(type(b_doc[0]))

b_annotations = b_doc[0].find_all("annotation")
print(b_annotations)


def get_all_occurences(text, doc):
    return [m.start() for m in re.finditer(text, doc)]


# def get_tokens(sent):
#     tokens = word_tokenize(sent)
#     token_index = []
#     cur_indx = 0
#     for i in range(0, len(tokens)-1):
#         token = tokens[i]
#         token_index.append(cur_indx)
#         cur_indx += len(token) + (0 if tokens[i+1] in [',', '.'] else 1)

#     return tokens, token_index

def get_tokens(txt):
    tokens = word_tokenize(txt)
    offset = 0
    token_indx_tuples = []
    for token in tokens:
        offset = txt.find(token, offset)
        token_indx_tuples.append((token, offset))
        offset += len(token)

    return token_indx_tuples


data = []
i = 0
for docs in b_doc:
    infon = docs.find("infon", {"key": "full_text"})
    document = infon.get_text().strip()
    data.append([])
    data[i].append(document)
    data[i].append({'entities': []})
    current_end = 0
    token_indx_tuples = get_tokens(document)
    for anots in docs.find_all("annotation"):
        word = anots.find("text").get_text()
        place = anots.find("location")
        offset = place["offset"]  # find the first occurence of this
        token, starting_index = token_indx_tuples[int(offset) - 1]
        length = place["length"]
        end = int(starting_index) + int(length)
        # print(document[starting_index:end])
        data[i][1]["entities"].append([starting_index, end, "INGREDIENT"])
        current_end = end
    i += 1
    # break

with open("FoodBase_uncurated_fixed.json", 'w') as outfile:
    json.dump(data, outfile)
