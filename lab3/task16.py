def calculate_average_imdb(movies):
    if not movies:
        return 0.0  

    total_score = sum(movie["imdb"] for movie in movies)
    average_score = total_score / len(movies)
    return average_score


movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    
]

average_imdb = calculate_average_imdb(movies)
print(f"The average IMDB score of the movies is: {average_imdb}")
