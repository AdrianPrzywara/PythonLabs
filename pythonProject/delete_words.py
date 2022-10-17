from pathlib import Path


def delete_words(path):
    with open(path, 'r', encoding="utf-8") as file:
        text = file.read()
    with open(path, 'w', encoding="utf-8") as file:
        for x in [' się', ' i', ' oraz', ' nigdy', ' dlaczego']:
            text = text.replace(x, '')
        file.write(text)


def change_words(path):
    with open(path, 'r', encoding="utf-8") as file:
        text = file.read()
    with open(path, 'w', encoding="utf-8") as file:
        pre_dictionary = {' i': '1', ' oraz': '2', ' nigdy': '3', ' dlaczego': '4'}
        dictionary = {'1': ' oraz', '2': ' i', '3': ' prawie nigdy', '4': ' czemu'}
        for x, y in pre_dictionary.items():
            text = text.replace(x, y)
        for x, y in dictionary.items():
            text = text.replace(x, y)
        file.write(text)


if __name__ == '__main__':
    p = Path('.')
    for i in (p.glob("*")):
        if i.suffix == '.txt':
            change_words(i)
