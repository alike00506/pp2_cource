def calculate_average_imdb_by_category(movies, category_name):
    category_movies = [movie["imdb"] for movie in movies if movie["category"] == category_name]

    if not category_movies:
        return 0.0 

    average_score = sum(category_movies) / len(category_movies)
    return average_score

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},

]

category_name = input("Enter a category name: ")
average_imdb_by_category = calculate_average_imdb_by_category(movies, category_name)
print(f"The average IMDB score for the category '{category_name}' is: {average_imdb_by_category}")
