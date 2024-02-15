def is_above_5_5(movie):
    return movie["imdb"] > 5.5

single_movie = {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
}

result = is_above_5_5(single_movie)
print(result) 
