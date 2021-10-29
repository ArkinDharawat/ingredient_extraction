import srsly
import typer
import warnings
from pathlib import Path

import spacy
from spacy.tokens import DocBin


def check_span_overlap(spans, span_tup):
    start, end = span_tup
    for span in spans:
        start_overlap = span[0] <= start <= span[1]
        end_overlap = span[0] <= end <= span[1]
        if start_overlap or end_overlap:
            return True
    return False


def convert(lang: str, input_path: Path, output_path: Path):
    nlp = spacy.blank(lang)
    db = DocBin()
    # print(srsly.read_json(input_path)[0])
    for text, annot in srsly.read_json(input_path):
        # print(text)
        doc = nlp.make_doc(text)
        ents = []
        spans_seen_so_far = set()
        for start, end, label in annot["entities"]:
            if (start, end) in spans_seen_so_far:
                continue  # seen this span so ignore it

            if check_span_overlap(spans_seen_so_far, (start, end)):
                # span exists
                continue

            spans_seen_so_far.add((start, end))
            span = doc.char_span(start, end, label=label)
            if span is None:
                msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
                warnings.warn(msg)
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)

    db.to_disk(output_path)


if __name__ == "__main__":
    typer.run(convert)
