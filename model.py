import pandas as pd
from joblib import dump
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import GradientBoostingClassifier


URL = "https://raw.githubusercontent.com/marcopeix/MachineLearningModelDeploymentwithStreamlit/refs/heads/master/18_caching_capstone/data/mushrooms.csv"
COLS = ['class', 'odor', 'gill-size', 'gill-color', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'ring-type', 'spore-print-color']

#Read Data
df=pd.read_csv(URL)
df=df[COLS]
print(df)


pipe=Pipeline([
    ('encoder',OrdinalEncoder()),
    ('gbc',GradientBoostingClassifier(max_depth=5,random_state=42))
])


#Fit the pipeline
X=df.drop(['class'],axis=1)
y=df['class']


pipe.fit(X,y)

#save the pipeline
dump(pipe,'model/pipe.joblib')


