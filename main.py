from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField
from request import api_request

app = Flask(__name__)
app.config["SECRET_KEY"] = 'lord_of_the_ringsu'

class MyForm(FlaskForm):
    choice = SelectField('Route', choices=['book', 'movie', 'character', 'chapter', 'quote'])


@app.route('/index')
@app.route("/", methods=["GET", "POST"])
def hello_world():
    form = MyForm()

    if form.validate_on_submit():
        choice = form.choice.data
        print(api_request(choice))
        if choice == 'book':
            return redirect(url_for('books'))
        elif choice == 'movie':
            return redirect(url_for('movies'))
        elif choice == 'character':
            return redirect(url_for('characters'))
        elif choice == 'chapter':
            return redirect(url_for('chapters'))
        elif choice == 'quote':
            return redirect(url_for('quotes'))
        return redirect('/')

    return render_template('index.html', form=form)


@app.route("/books", methods=["GET"])
def books():
    response = api_request('book')

    print(response['docs'])
    return render_template('books.html', books=response['docs'])


@app.route('/book_chapters/<id>')
def book_chapters(id):
    response = api_request(f'book/{id}/chapter')
    print(response)

    return render_template('book_chapters.html', chapters=response['docs'])


@app.route('/movies')
def movies():
    response = api_request('movie')
    print(response)

    return render_template('movies.html', movies=response['docs'])


@app.route('/movie_info/<id>')
def movie_info(id):
    response = api_request(f'movie/{id}')

    print(response)

    return render_template('movie_info.html', movie=response['docs'])


@app.route('/movie_quotes/<id>')
def movie_quotes(id):
    response = api_request(f'movie/{id}/quote')

    print(response)

    return render_template('movie_quotes.html', quotes=response['docs'])


@app.route('/characters')
def characters():
    response = api_request(f'character')

    print(response)

    return render_template('characters.html', characters=response['docs'])


@app.route('/chapters')
def chapters():
    response = api_request(f'chapter')

    return render_template('chapters.html', chapters=response['docs'])


@app.route('/quotes')
def quotes():
    response = api_request(f'quote')

    print(response)

    return render_template('quotes.html', quotes=response['docs'])

if __name__ == '__main__':
    app.run(debug=True)
