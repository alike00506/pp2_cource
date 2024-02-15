def get_movies_by_category(category_name):
    movies = [
        {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
        {"name": "Hitman", "imdb": 6.3, "category": "Action"},
        {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
        {"name": "The Help", "imdb": 8.0, "category": "Drama"},
        {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
        # ... (other movies in the list)
    ]

    movies_in_category = [movie for movie in movies if movie["category"] == category_name]
    return movies_in_category

# Example usage:
category_name = input("Enter a category name: ")
movies_in_category = get_movies_by_category(category_name)
print(f"Movies in the category '{category_name}':")
print(movies_in_category)
