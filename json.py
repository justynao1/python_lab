import json

def read_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

def write_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)

def add_data(data):
    title = input("Enter the title of the movie: ")
    director = input("Enter the director of the movie: ")
    year = input("Enter the year of the movie: ")
    genre = input("Enter the genre of the movie: ")
    rating = input("Enter the rating of the movie: ")
    data[title] = {"director": director, "year": year, "genre": genre, "rating": rating}
    return data

def delete_data(data):
    title = input("Enter the title of the movie: ")
    if title in data:
        del data[title]
    else:
        print("There is no such movie in the database.")
    return data

def parser():
    data = read_data()
    print("Welcome to the movie database!")
    while True:
        print("1. Add a movie")
        print("2. Delete a movie")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            data = add_data(data)
            write_data(data)
        elif choice == "2":
            data = delete_data(data)
            write_data(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
parser()