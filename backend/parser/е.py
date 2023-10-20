from pprint import pprint
import csv
import re
from collections import defaultdict

# Тут делаю заготовку парсера заклинаний что бы сразу к классам была привязка

d = defaultdict(int)


def remove_brackets(text):
    cleaned_text = re.sub(r'\([^()]+\)', '', text)
    return cleaned_text.strip()


def extract_contents(text):
    pattern = r'\(([^()]+)\)'
    matches = re.findall(pattern, text)

    for match in matches:
        text = text.replace(f'({match})', '')

    return text.strip(), matches


def combine_names():
    x = 0
    with open(
            'spells.csv',
            'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            x += 1
            class_ch = row[8].split(',')
            for i in class_ch:
                i = remove_brackets(i)
                # d[i.strip()] += 1
            # pprint(sorted(d.items()))

            y = row[9].split(',')
            for i in y:
                text_before, contents = extract_contents(i.strip())
                # print(contents)
                print(f"{text_before} - "+"-".join(contents))



combine_names()
