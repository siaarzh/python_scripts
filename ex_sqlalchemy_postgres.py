import pandas as pd
from sqlalchemy import create_engine


# Create a database called "movielens" for this to work
engine = create_engine('postgresql://postgres:password@localhost:5432/movielens')

# Movies
# index_col selects the index column so that pandas does not have to create a separate one
df = pd.read_csv(r'C:\PROJECTS\w\movielens_rec_flask\datasets\ml-latest-small\movies.csv', index_col='movieId')
df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces

df.to_sql("movies", engine)

# Ratings
df = pd.read_csv(r'C:\PROJECTS\w\movielens_rec_flask\datasets\ml-latest-small\ratings.csv', index_col="userId")
df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

df.to_sql("ratings", engine)
