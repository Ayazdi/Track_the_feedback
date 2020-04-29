import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sqlalchemy import create_engine




def vectorize_train):
    df = pd.read_csv("Sarcasm_Headlines_Dataset.csv")
    X = df['headline']
    y = df['is_sarcastic']

    tv = TfidfVectorizer(max_features=5000, ngram_range=(1, 1), lowercase=True)
    X = list(X)
    X = tv.fit_transform(X).toarray()
    lsvc = LinearSVC()
    lsvc.fit(X, y)

    return(lsvc, tv)


def predict_sarcasm(tweet, lsvc, tv):
    tweet = tv.transform([tweet]).toarray()
    y_pred = lsvc.predict(tweet)
    return y_pred
