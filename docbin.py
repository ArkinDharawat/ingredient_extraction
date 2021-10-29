import spacy
from spacy.training import Example
from spacy.tokens import DocBin
import json


with open("FoodBase_curated_fixed.json") as json_file:
    td = json.load(json_file)

nlp = spacy.blank("en")
db = DocBin()

for text, annotations in td:
    example = Example.from_dict(nlp.make_doc(text), annotations)
    db.add(example.reference)

db.to_disk("td.spacy")