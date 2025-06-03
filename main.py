from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Card 1 Title", "Some quick example text to build on the card title and make up the bulk of the card's content.", "Go somewhere", "static/images/logo.png"),
        ("Card 2 Title", "Some quick example text to build on the card title and make up the bulk of the card's content.", "Go somewhere", "static/images/logo.png"),
        ("Card 3 Title", "Some quick example text to build on the card title and make up the bulk of the card's content.", "Go somewhere", "static/images/logo.png"),
        ("Card 4 Title", "Some quick example text to build on the card title and make up the bulk of the card's content.", "Go somewhere", "static/images/logo.png"),
        ("Card 5 Title", "Some quick example text to build on the card title and make up the bulk of the card's content.", "Go somewhere", "static/images/logo.png"),
        ("Card 6 Title", "Some quick example text to build on the card title and make up the bulk of the card's content.", "Go somewhere", "static/images/logo.png")
    )
    return render_template("index.html", cards=card_data), 200


@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200


if __name__ == '__main__':
    app.run(debug=True)
