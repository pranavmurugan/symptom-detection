import numpy as np
import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer 
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('df_unique.csv') 

def my_cool_preprocessor(text):  
    print('lower case')
    text=text.lower() 
    print('remove special characters')
    text=re.sub("\\W"," ",text) # remove special characters
    
    print('finished')
    return text

#fit count vectorizer
corpus = df["turn_text"]
count_vec = CountVectorizer(stop_words='english', preprocessor = my_cool_preprocessor, max_features = 1000)
count_data = count_vec.fit_transform(corpus)

#obtain count vectorized data 
cv_data = pd.DataFrame(count_data.toarray(), columns = count_vec.get_feature_names_out())
cv_data.to_csv('cv_data.csv', index = False)