# WK6Lab2 – Movie Guide - Part 2
# Course no: CIS 261
# Name: Terrence Miller

import os

def get_menu_choice():
    """
    Get menu choice from user
    """
    choice = input("Command: ")
    return choice

def display_menu():
    """
    Display menu
    """
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")

def display_all_movies(movies):
    """
    Display all movies
    """
    print("All Movies")
    print("----------")
    n = 1
    for movie in movies:
        print(n,".",movie)
        n += 1

def add_movie(movies):
    """
    Add a movie
    """
    movie = input("movie: ")
    movies.append(movie)
    print(movie," was added")
    save_movies(movies)

def delete_movie(movies):
    """
    Delete a movie
    """
    display_all_movies(movies)
    movie_number = int(input("Number: "))
    if len(movies) > movie_number  - 1:
        movie = movies[movie_number - 1]
        del movies[movie_number  - 1]
        print(movie," was deleted")
    else:
        print("Movie not found")
    save_movies(movies)

def save_movies(movies):
    """
    Save movies
    """
    with open("movies.txt", "w") as file:
        for movie in movies:
            file.write(movie + "\n")

def load_movies(movies):
    """
    Load movies
    """
    if os.path.isfile("movies.txt"):
        with open("movies.txt", "r") as file:
            for line in file:
                movies.append(line.strip())

def main():
    """
    Main function
    """
    print("The Movie List Program")
    print("----------------------")
    movies = []
    load_movies(movies)
    while True:
        display_menu()
        choice = get_menu_choice()
        if choice == "list":
            display_all_movies(movies)
        elif choice == "add":
            add_movie(movies)
        elif choice == "del":
            delete_movie(movies)
        elif choice == "exit":
            print("\n")
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
main() 


























