# create_reference.py
from sklearn.datasets import load_wine
import pandas as pd

wine = load_wine()

X = wine.data
y = wine.target

df = pd.DataFrame(X, columns=wine.feature_names)

df.to_csv("data/reference_data.csv", index=False)

print("Reference dataset created!")