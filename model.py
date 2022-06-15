import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

df = pd.read_csv('hiring.csv')
df['experience'].fillna(0,inplace=True)
df['test_score(out of 10)'].fillna(df['test_score(out of 10)'].mean(),inplace=True)

X = df.iloc[:,:-1]
y = df.iloc[:,-1:]

def convert_to_int(exp):
    word_dict = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,0:0}
    return word_dict[exp]

X['experience'] = X['experience'].apply(lambda x:convert_to_int(x))

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,y)

pickle.dump(model, open('model.pkl','wb'))