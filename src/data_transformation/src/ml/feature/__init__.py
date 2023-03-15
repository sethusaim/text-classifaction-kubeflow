import re
import string

import nltk
import spacy
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer

from src.constant import training_pipeline

regexp = RegexpTokenizer("[\w']+")

stemmer = PorterStemmer()

stops = stopwords.words("english")

spacy_lemmatizer = spacy.load("en_core_web_sm", disable=["parser", "ner"])

all_stopwords = stops + training_pipeline.DATA_TRANSFORMATION_STOP_WORDS

additional_stops = (
    training_pipeline.ALPHABETS
    + training_pipeline.PREPOSITIONS
    + training_pipeline.PREPOSITIONS_LESS_COMMON
    + training_pipeline.COORDINATING_CONJUNCTIONS
    + training_pipeline.CORRELATIVE_CONJUNCTIONS
    + training_pipeline.SUBORDINATING_CONJUNCTIONS
    + training_pipeline.OTHERS
)


convert_to_lowercase = lambda text: text.lower()

remove_whitespace = lambda text: text.strip()

remove_punctuation = lambda text: text.translate(
    str.maketrans("", "", string.punctuation.replace("'", ""))
)

remove_html = lambda text: re.compile(r"<.*?>").sub(r"", text)

remove_emoji = lambda text: re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "]+",
    flags=re.UNICODE,
).sub(r"", text)

remove_http = lambda text: re.sub(r"({})".format("https?://\S+|www\.\S+"), "", text)


def convert_acronyms(text: str, acronyms_dict: dict) -> str:
    words = []

    acronyms_list = list(acronyms_dict.keys())

    for word in regexp.tokenize(text):
        if word in acronyms_list:
            words = words + acronyms_dict[word].split()
        else:
            words = words + word.split()

    text_converted = " ".join(words)

    return text_converted


def convert_contractions(text: str, contractions_dict: dict):
    words = []

    contractions_list = list(contractions_dict.keys())

    for word in regexp.tokenize(text):
        if word in contractions_list:
            words = words + contractions_dict[word].split()

        else:
            words = words + word.split()

    text_converted = " ".join(words)

    return text_converted


remove_stopwords = lambda text: " ".join(
    [word for word in regexp.tokenize(text) if word not in all_stopwords]
)

text_stemmer = lambda text: " ".join(
    [stemmer.stem(word) for word in regexp.tokenize(text)]
)

text_lemmatizer = lambda text: " ".join(
    [token.lemma_ for token in spacy_lemmatizer(text)]
)

discard_non_alpha = lambda text: " ".join(
    [word for word in regexp.tokenize(text) if word.isalpha()]
)


def keep_pos(text):
    tokens = regexp.tokenize(text)

    tokens_tagged = nltk.pos_tag(tokens)

    keep_words = [
        x[0]
        for x in tokens_tagged
        if x[1] in training_pipeline.DATA_TRANSFORMATION_KEEP_TAGS
    ]

    return " ".join(keep_words)


remove_additional_stopwords = lambda text: " ".join(
    [word for word in regexp.tokenize(text) if word not in additional_stops]
)


def text_normalizer(text: str, acronyms_dict: dict, contractions_dict: dict):
    text = convert_to_lowercase(text)

    text = remove_whitespace(text)

    text = re.sub("\n", "", text)  # converting text to one line

    text = re.sub("\[.*?\]", "", text)  # removing square brackets

    text = remove_http(text)

    text = remove_punctuation(text)

    text = remove_html(text)

    text = remove_emoji(text)

    text = convert_acronyms(text, acronyms_dict)

    text = convert_contractions(text, contractions_dict)

    text = remove_stopwords(text)

    text = text_lemmatizer(text)

    text = discard_non_alpha(text)

    text = keep_pos(text)

    text = remove_additional_stopwords(text)

    return text
