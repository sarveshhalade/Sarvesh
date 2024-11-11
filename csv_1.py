import pandas as pd

df = pd.read_csv('C:/Users/Sarvesh/Downloads/people-100.csv')
s=df[['Index','User Id','First Name']]
print(s)
