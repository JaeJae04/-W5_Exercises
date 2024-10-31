# Create a list with the titles of your favorite movies (or movies you’d like to watch

favorite_movies = ['endlesslove', 'Scary movie 2', 'Venom']

print('The list fave_movies includes my top ' + str(len) + ' favorite movies')
# result = The list fave_movies includes my top <built-in function len> favorite movies

print(f"This'movies' are my top {len(favorite_movies)} favorite movies of all time:{", ".join(favorite_movies)}")
# result = my top 3 favorite movies of all time:endlesslove, Scary movie 2, Venom

print('The list ' + str(favorite_movies) + ' includes my top ' + str((len(favorite_movies))) + ' favorite movies')
# result = The list ['endlesslove', 'Scary movie 2', 'Venom'] includes my top 3 favorite movies

print(sorted(favorite_movies))
print(favorite_movies)

# 2 diffrent results ['Scary movie 2', 'Venom', 'endlesslove']['endlesslove', 'Scary movie 2', 'Venom']

favorite_movies.sort()
print(favorite_movies)

# sorted in alphabetical order

# Think of at least one more movie to add to your list, and use the .append() method to 
# add it. Then print the list again, also including an updated description statement.

favorite_movies.append('Fast and Furious')
print(favorite_movies)

print('The list fave_movies includes my top ' + str((len(favorite_movies))) + ' favorite movies')
print('The list ' + str(favorite_movies) + ' includes my top ' + str((len(favorite_movies))) + ' favorite movies') 