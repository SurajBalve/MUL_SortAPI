import pandas as pd
import numpy as np
import pickle
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix

df=pd.read_csv("C:\\artin\\ML_data_Traning\\spam_ham_dataset.csv")

def clean_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Remove digits
    text = re.sub(r'\d+', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

df['cleaned_text'] = df['text'].apply(clean_text)

X= df['cleaned_text']
y = df['label_num']
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size= 0.2,random_state= 42)

vectorizer = TfidfVectorizer(stop_words='english')# Remove common English stopwords
X_tran=vectorizer.fit_transform(X)
with open('vectorizer.pkl','wb') as f:
    pickle.dump(vectorizer,f)
# X_train_tfidf = vectorizer.fit_transform(X_train)
# X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_tran,y)

with open ('model.pkl','wb')as f:
    pickle.dump(model,f)