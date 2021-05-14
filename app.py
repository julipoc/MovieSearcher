from flask import Flask, render_template, request
from imdb import IMDb

app = Flask(__name__)
instance = IMDb()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/movies", methods=["GET", "POST"])
def movies():
    if request.method == "POST":
        search = request.form.get("name")
        movie = instance.search_movie(str(search))

        movie_three = []

        for i in range(len(movie)):
            id_number = movie[i].movieID
            movie_two = instance.get_movie(id_number)
            movie_three.append(movie_two)

        return render_template("movies.html", movie=movie, movie_three=movie_three)
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
