from pathlib import Path


def delete_word(path, word_to_delete):
    text = path.read_text()
    text = text.split(' ')
    for word in text:
        if word == word_to_delete:



if __name__ == '__main__':
    p = Path('.')
    delete_word(p, "ale")