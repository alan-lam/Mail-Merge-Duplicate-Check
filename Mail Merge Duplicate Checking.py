import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/1G_brFiEo_rj4634mxpDGFCQY4VGgSXbqw9o1nBu9bFE/export?gid=0&format=csv', names=['company', 'email'])
df.index = range(1, len(df) + 1)

print(df[df.duplicated(['email']) == True])
