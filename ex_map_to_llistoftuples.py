sample = "1,2\n3,4\n5,6"

with open('user_ratings.file', "r") as f:

    ratings_list = f.read().strip().split("\n")

ratings_list = list(map(lambda x: x.split(","), ratings_list))
ratings = list(map(lambda x: ("3", int(x[0]), float(x[1])), ratings_list))

print(ratings)