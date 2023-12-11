# Chapter 1 Exercise 10 : Film Dictionary

# Creating a film dictionary
film = {
    "Title": "Inception",
    "Director": "Christopher Nolan",
    "Year": 2010,
    "Genre": "Sci-Fi",
    "Rating": 8.8
}

# Displaying film details using a loop
print("Film Details:")
for key, value in film.items():
    print(f"{key}: {value}")