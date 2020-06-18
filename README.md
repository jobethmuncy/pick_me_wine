<h1>Project 5 - Capstone</h1>
<h3>Problem Statement</h3>
The world of wine can be confusing to navigate. Every country different rules and regulations for labeling and selling wines. A wine label itself can be difficult to read. If someone knows one or two words about a flavor profile, producer, grape, vineyard site, region, appellation how do they find that wine or other similar ones? I am creating a wine recommender that will take text and recommend wines that are available to purchase with a link to the site so they can buy and explore.<br>
<h3>Data Collecting</h3>
<ul>
    <li>https://www.chambersstwines.com/</li>
    <li>https://www.astorwines.com/</li>
    <li>https://2020wines.com/</li>
    <li>https://www.wine.com/</li>
</ul>


<h4>Capstone</h4>
    <ul><strong>app</strong>
        <li>templates</li>
            -results.html<br>
            -search_form.html
        <li>testing_py_functions</li>
        <li>model.all</li>
        <li>model.other</li>
        <li>model.red</li>
        <li>model.rose</li>
        <li>model.sparkling</li>
        <li>model.white</li>
        <li>names_as_columns.csv</li>
        <li>model.red</li>
        <li>model.rose</li>
        <li>other_flask.csv</li>
        <li>red_flask.csv</li>
        <li>rose_flask.csv</li>
        <li>search_functions.py</li>
        <li>sparkling_flask.csv</li>
        <li>white_flask.csv</li>
        <li>wine_app.py</li>
    </ul>
    <ul><strong>code</strong>
        <li>01_astor_producer_scraping.ipynb</li>
        <li>02_astor_wines_scraping.ipynb</li>
        <li>03_chambers_scraping.ipynb</li>
        <li>04_2020_wines_scraping.ipynb</li>
        <li>05_wine_com_scraping.ipynb</li>
        <li>06_Cleaning_EDA.ipynb</li>
        <li>07_fasttext_recommender.ipynb</li>
    </ul>
    <ul><strong>data</strong>
        <li>2020_wines</li>
        <li>all_clean_wines.csv</li>
        <li>all_wines.csv</li>
        <li>astor_data</li>
        <li>astor_txt</li>
        <li>chambers_street</li>
        <li>recommender_flask.csv</li>
        <li>test_lower_wines.csv</li>
        <li>test_wines.csv</li>
        <li>wine_com</li>
    </ul>
        <ul><strong>images</strong>
        <li>all_countries.png</li>
        <li>by_color.png</li>
        <li>merkle</li>
        <li>mosel</li>
        <li>riffault</li>
        <li>saint_joseph</li>
        <li>twenty.png</li>
        <li>wine.png</li>
    </ul>
    Pick me a Wine.pdf<br>
    README.md
    
<h3>Executive Statement</h3>
Data was gathered from four different websites. None of them had API’s and all the scraping was done using python functions and for loops. Because this data was from different sources, each set had unique challenges when it came to data cleaning and feature engineering. There were 11,767 wines total used in the Flask recommender. Many of these wines had sections that were misclassified. Grapes listed as regions, regions listed as countries, styles of wine listed as grape, many of these were corrected but there is still some to be done like correcting vintages and some prices. 
<br>The color, grape, country, region and text description were combined into one column. This data had stopwords, punctuation, and capitalization removed before applying FastText to the corpus. I wanted a recommender to take a string of text and generate similarities. FastText will do exactly that. It is pre-trained on 1 Million words and can infer similar words from rare words, made up word, or misspelled words. this word embedding was used to generate 3 words that were similar to the user input then find wines that also contained these words and return those results to the user.<br>
This had some limitations as only one value per similar wine was returned. I wanted the user to have the name, url, and price of each wine so the DataFrame was transposed so the name of the wines could be called on all the other values. To randomize the results, numpy was used to return 5 different wines to the user. <br> Initially the recommender did not pull things that I would consider to be good results. Many wines of various styles will use similar key terms and breaking up the DataFrame by wine color acted as a first filter for the user. The wines returned made sense when filtered this way. 

<h3>Conclusion</h3> 
Overall, the wine recommender brought back reasonable selections given the user input. It found wines with similar text based descriptors from Astor, Chambers, Twenty Twenty, and Wine.com providing the user with the words generated for the search, name, price and url of the selection. Each page provides the user with like wines to even further broaden their tree of similar wines. 

<h3>Further Development</h3>
I am new to the world of HTML so the Flask app will be cleaned up to make it more user friendly and styled. These is a much high number of red wines so I would like to find sites that feature more white, sparkling, rose, and other wines to even out the data sets. If these were more balanced, I would like to see how the model performs on the whole set rather than slices by color.<br>Further cleaning the data to indicate organic, natural, biodynamic, orange, no sulfur and so on would be a breakdown that would be interesting as a filtering function. I would also like to be able to return results by price range to the user. As a last step, including data from restaurants would be my goal so the user could find and enjoy the selections locally. 
