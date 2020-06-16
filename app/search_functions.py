# imports
import pandas as pd
import numpy as np
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import gensim
from gensim.models import FastText
import fasttext
from flask import Flask, Response, request, jsonify, render_template

# bring in data 
all_df = pd.read_csv('./for_flask.csv')
red_df = pd.read_csv('./red_flask.csv')
white_df = pd.read_csv('./white_flask.csv')
rose_df = pd.read_csv('./rose_flask.csv')
sparkling_df = pd.read_csv('./sparkling_flask.csv')
other_df = pd.read_csv('./other_flask.csv')
names = pd.read_csv('./names_as_columns.csv')

# bring in modesls
fast_text_red = pickle.load(open('model.red', 'rb'))
fast_text_white = pickle.load(open('model.white', 'rb'))
fast_text_rose = pickle.load(open('model.rose', 'rb'))
fast_text_sparkling = pickle.load(open('model.sparkling', 'rb'))
fast_text_other = pickle.load(open('model.other', 'rb'))

# instanciate lemmatizer
lemmatizer = WordNetLemmatizer()

# RED WINES
def what_are_words(values):
    user_input = str(values)
    fast_input = fast_text_red.wv.most_similar([user_input], topn=5)
    user_input_word = [i[0] for i in fast_input]
    check_for_similar = [lemmatizer.lemmatize(w) for w in user_input_word]
    unique = set(check_for_similar)
    return fast_input, unique

def red_matches(values):
    user_input = str(values)
    fast_input = fast_text_red.wv.most_similar([user_input], topn=3)
    user_input = [i[0] for i in fast_input]
    check_for_similar = [lemmatizer.lemmatize(w) for w in user_input]
    unique = set(check_for_similar)
    for word in unique: 
        contains_word = red_df[red_df['description_clean'].str.contains(word)]['name']

        wines_with_words = []
        for wine in contains_word:
            wines_with_words.append(wine)
    return np.random.choice(wines_with_words, 5, replace=False).tolist()

# WHITE WINES
def what_are_words_white(values):
    user_input = str(values)
    fast_input = fast_text_white.wv.most_similar([user_input], topn=5)
    user_input_word = [i[0] for i in fast_input]
    check_for_similar = [lemmatizer.lemmatize(w) for w in user_input_word]
    unique = set(check_for_similar)
    return fast_input, unique

def white_matches(values):
    user_input = str(values)
    fast_input = fast_text_white.wv.most_similar([user_input], topn=3)
    user_input = [i[0] for i in fast_input]
    check_for_similar = [lemmatizer.lemmatize(w) for w in user_input]
    unique = set(check_for_similar)
    for word in unique: 
        contains_word = white_df[white_df['description_clean'].str.contains(word)]['name']

        wines_with_words = []
        for wine in contains_word:
            wines_with_words.append(wine)
    return np.random.choice(wines_with_words, 5, replace=False).tolist()

# ROSE
def what_are_words_rose(values):
    user_input = str(values)
    fast_input = fast_text_rose.wv.most_similar([user_input], topn=5)
    user_input_word = [i[0] for i in fast_input]
    check_for_similar = [lemmatizer.lemmatize(w) for w in user_input_word]
    unique = set(check_for_similar)
    return fast_input, unique

def rose_matches(values):
    user_input = str(values)
    fast_input = fast_text_rose.wv.most_similar([user_input], topn=3)
    user_input = [i[0] for i in fast_input]
    check_for_similar = [lemmatizer.lemmatize(w) for w in user_input]
    unique = set(check_for_similar)
    for word in unique: 
        contains_word = rose_df[rose_df['description_clean'].str.contains(word)]['name']

        wines_with_words = []
        for wine in contains_word:
            wines_with_words.append(wine)
    return np.random.choice(wines_with_words, 5, replace=False).tolist()

# SPARKLING
def what_are_words_sparkling(values):
    user_input = str(values)
    fast_input = fast_text_sparkling.wv.most_similar([user_input], topn=5)
    user_input_word = [i[0] for i in fast_input]
    check_for_similar = [lemmatizer.lemmatize(w) for w in user_input_word]
    unique = set(check_for_similar)
    return fast_input, unique

def sparkling_matches(values):
    user_input = str(values)
    fast_input = fast_text_sparkling.wv.most_similar([user_input], topn=3)
    user_input = [i[0] for i in fast_input]
    check_for_similar = [lemmatizer.lemmatize(w) for w in user_input]
    unique = set(check_for_similar)
    for word in unique: 
        contains_word = sparkling_df[sparkling_df['description_clean'].str.contains(word)]['name']

        wines_with_words = []
        for wine in contains_word:
            wines_with_words.append(wine)
    return np.random.choice(wines_with_words, 5, replace=False).tolist()

# OTHER
def what_are_words_other(values):
    user_input = str(values)
    fast_input = fast_text_other.wv.most_similar([user_input], topn=5)
    user_input_word = [i[0] for i in fast_input]
    check_for_similar = [lemmatizer.lemmatize(w) for w in user_input_word]
    unique = set(check_for_similar)
    return fast_input, unique

def other_matches(values):
    user_input = str(values)
    fast_input = fast_text_other.wv.most_similar([user_input], topn=3)
    user_input = [i[0] for i in fast_input]
    check_for_similar = [lemmatizer.lemmatize(w) for w in user_input]
    unique = set(check_for_similar)
    for word in unique: 
        contains_word = other_df[other_df['description_clean'].str.contains(word)]['name']

        wines_with_words = []
        for wine in contains_word:
            wines_with_words.append(wine)
    return np.random.choice(wines_with_words, 5, replace=False).tolist()
