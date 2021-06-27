import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import ComplementNB, MultinomialNB
import pickle
import nltk
nltk.download("stopwords", quiet=True) # helps us get rid of stop words
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

df = pd.read_csv("text_preprocessed.csv")
df = df.iloc[:,1:]
# df = df[["text", "label"]]
# print(df.head())
# df["label"] = df["label"].map({'real': 0, 'fake':1})
# # #print(df["label"].unique())
# df = df.dropna(axis=0, how='any')
# X = df["text"].tolist()
# y = df["label"].tolist()
# # df.loc[df.label == 1,:].head()
X = df.text
y = df.label
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, train_size=0.75,random_state=0)

#X_train, X_val, y_train, y_val = train_test_split(X_train,y_train, test_size=0.25, random_state=0)
cv = CountVectorizer(stop_words=stopwords.words("english"))
cv.fit(X_train)
X_train = cv.transform(X_train) 
X_test = cv.transform(X_test) 
# feature_names = cv.get_feature_names()

model = ComplementNB()
model.fit(X_train, y_train)


pickle.dump(cv, open('countercm.pkl', 'wb'))
pickle.dump(model, open('modelcm.pkl','wb'))

