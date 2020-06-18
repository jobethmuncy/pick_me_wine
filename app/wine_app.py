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
from search_functions import what_are_words, red_matches, what_are_words_white, white_matches, \
    what_are_words_rose, rose_matches, what_are_words_sparkling, sparkling_matches, \
        what_are_words_other, other_matches

# flask app
app = Flask('Find_me_Wines')

# pages 
red_df = pd.read_csv('./red_flask.csv')
names = pd.read_csv('./names_as_columns.csv')

# base url - local host 
@app.route('/')
def form():
    return render_template('search_form.html')

@app.route('/red')
def red(): 
    user_input = request.args
    response = user_input['user_input_red']
    wines = red_matches(response)
    best_fit = what_are_words(response)
    return render_template('results.html', what_listed = response, 
                            best_fit0=best_fit[0][0], best_fit1=best_fit[0][1], best_fit2=best_fit[0][2],
                            wine0=wines[0], wine1=wines[1], wine2=wines[2], wine3=wines[3], wine4=wines[4], 
                            url0=names[wines[0]][0], url1=names[wines[1]][0], url2=names[wines[2]][0], 
                            url3=names[wines[3]][0], url4=names[wines[4]][0],
                            price0=names[wines[0]][1], price1=names[wines[1]][1], price2=names[wines[2]][1],
                            price3=names[wines[3]][1], price4=names[wines[4]][1], 
                            country0=names[wines[0]][2], country1=names[wines[1]][2], country2=names[wines[2]][2],
                            country3=names[wines[3]][2], country4=names[wines[4]][2] ) 
    
@app.route('/white')
def white():
    user_input = request.args
    response = user_input['user_input_white']
    wines = white_matches(response)
    best_fit = what_are_words_white(response)
    return render_template('results.html', what_listed = response, 
                            best_fit0=best_fit[0][0], best_fit1=best_fit[0][1], best_fit2=best_fit[0][2], 
                            wine0=wines[0], wine1=wines[1], wine2=wines[2], wine3=wines[3], wine4=wines[4], 
                            url0=names[wines[0]][0], url1=names[wines[1]][0], url2=names[wines[2]][0], 
                            url3=names[wines[3]][0], url4=names[wines[4]][0],
                            price0=names[wines[0]][1], price1=names[wines[1]][1], price2=names[wines[2]][1],
                            price3=names[wines[3]][1], price4=names[wines[4]][1], 
                            country0=names[wines[0]][2], country1=names[wines[1]][2], country2=names[wines[2]][2],
                            country3=names[wines[3]][2], country4=names[wines[4]][2] ) 

@app.route('/rose')
def rose():
    user_input = request.args
    response = user_input['user_input_rose']
    wines = rose_matches(response)
    best_fit = what_are_words_rose(response)
    return render_template('results.html', what_listed = response, 
                            best_fit0=best_fit[0][0], best_fit1=best_fit[0][1], best_fit2=best_fit[0][2],
                            wine0=wines[0], wine1=wines[1], wine2=wines[2], wine3=wines[3], wine4=wines[4], 
                            url0=names[wines[0]][0], url1=names[wines[1]][0], url2=names[wines[2]][0], 
                            url3=names[wines[3]][0], url4=names[wines[4]][0],
                            price0=names[wines[0]][1], price1=names[wines[1]][1], price2=names[wines[2]][1],
                            price3=names[wines[3]][1], price4=names[wines[4]][1], 
                            country0=names[wines[0]][2], country1=names[wines[1]][2], country2=names[wines[2]][2],
                            country3=names[wines[3]][2], country4=names[wines[4]][2] ) 

@app.route('/sparkling')
def sparkling():
    user_input = request.args
    response = user_input['user_input_sparkling']
    wines = sparkling_matches(response)
    best_fit = what_are_words_sparkling(response)
    return render_template('results.html', what_listed = response, 
                            best_fit0=best_fit[0][0], best_fit1=best_fit[0][1], best_fit2=best_fit[0][2], 
                            wine0=wines[0], wine1=wines[1], wine2=wines[2], wine3=wines[3], wine4=wines[4], 
                            url0=names[wines[0]][0], url1=names[wines[1]][0], url2=names[wines[2]][0], 
                            url3=names[wines[3]][0], url4=names[wines[4]][0],
                            price0=names[wines[0]][1], price1=names[wines[1]][1], price2=names[wines[2]][1],
                            price3=names[wines[3]][1], price4=names[wines[4]][1], 
                            country0=names[wines[0]][2], country1=names[wines[1]][2], country2=names[wines[2]][2],
                            country3=names[wines[3]][2], country4=names[wines[4]][2] ) 

@app.route('/other')
def other():
    user_input = request.args
    response = user_input['user_input_other']
    wines = other_matches(response)
    best_fit = what_are_words_other(response)
    return render_template('results.html', what_listed = response, 
                            best_fit0=best_fit[0][0], best_fit1=best_fit[0][1], best_fit2=best_fit[0][2], 
                            wine0=wines[0], wine1=wines[1], wine2=wines[2], wine3=wines[3], wine4=wines[4], 
                            url0=names[wines[0]][0], url1=names[wines[1]][0], url2=names[wines[2]][0], 
                            url3=names[wines[3]][0], url4=names[wines[4]][0],
                            price0=names[wines[0]][1], price1=names[wines[1]][1], price2=names[wines[2]][1],
                            price3=names[wines[3]][1], price4=names[wines[4]][1], 
                            country0=names[wines[0]][2], country1=names[wines[1]][2], country2=names[wines[2]][2],
                            country3=names[wines[3]][2], country4=names[wines[4]][2] ) 















if __name__ == '__main__':
    app.run(debug=True)
