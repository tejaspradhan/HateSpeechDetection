from numpy.matrixlib.defmatrix import matrix
from tensorflow.keras.models import load_model
import os  # accessing directory structure
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import json
import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing import sequence


def image_classification():
    pass


def text_classification(text):
    with open('tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    matrix = tokenizer.texts_to_matrix([text])
    sequences = sequence.pad_sequences(matrix, maxlen=1000)
    print(sequences.shape)
    model = load_model('text_classification_model.h5')
    prob = model.predict(sequences)
    return prob


def preprocess(text):
    stop_words = stopwords.words('english')
    lem = WordNetLemmatizer()
    text = re.sub('[^A-Za-z]+', ' ', text).lower()
    text = "".join([i.lower()
                    for i in text if i not in string.punctuation])
    tokens = word_tokenize(text)
    cleanText = ''
    for token in tokens:
        if(token not in stop_words):
            cleanText += lem.lemmatize(token) + " "
    return cleanText
