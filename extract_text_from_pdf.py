import fitz
import nltk
from pathlib import Path
from nltk.corpus import stopwords
import pandas as pd

"""
http://www.nltk.org/nltk_data/
"""


def print_options():
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.width', None)


data_dir = Path.cwd() / 'data'
nltk.data.path.append(str(data_dir))


def get_text():
    """
    Read the PDF and generate word tokens
    :return: list of words
    """
    doc = fitz.open(str(data_dir / 'marco_parolini.pdf'))
    word_list = []
    for page_num in range(doc.pageCount):
        page = doc.load_page(page_id=page_num)
        text = page.get_text()
        tokens = nltk.word_tokenize(text)
        for item in tokens:
            if item.isalnum():
                word_list.append(item.lower())

    return list(set(word_list))


def remove_stop_words():
    """
    Remove stop words from the word list
    :return: list of words
    """
    stop_words = set(stopwords.words('english'))
    word_list = get_text()
    filtered_list = []
    for word in word_list:
        if word not in stop_words:
            filtered_list.append(word)
    return filtered_list


def remove_small_words():
    """
    Remove small words and generate pickle file
    :return: Dataframe pickle
    """
    filtered_list = remove_stop_words()
    word_list = []
    for word in filtered_list:
        if len(word) >= 4:
            word_list.append(word)
    data = {
        'word_list': word_list
    }
    df = pd.DataFrame(data=data)
    df.to_pickle(str(data_dir / 'word_list.pkl'))
    return word_list


if __name__ == '__main__':
    remove_small_words()
