from flask import Flask, render_template, request

app = Flask(__name__)

player = 0


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/game/", methods=["GET", "POST"])
def game():
    game = request.form["number"]
    list = [301]* int(game)
    return render_template("game.html", list = list)


if __name__ == "__main__":
    app.run(debug=True)