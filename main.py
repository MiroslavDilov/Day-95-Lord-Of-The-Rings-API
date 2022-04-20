from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField
from request import api_request

app = Flask(__name__)
app.config["SECRET_KEY"] = 'lord_of_the_ringsu'

class MyForm(FlaskForm):
    choice = SelectField('Route', choices=['book', 'movie', 'character', 'chapter'])


@app.route('/index')
@app.route("/", methods=["GET", "POST"])
def hello_world():
    form = MyForm()

    if form.validate_on_submit():
        choice = form.choice.data
        print(api_request(choice))
        if choice == 'book':
            return redirect(url_for('books'))
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


if __name__ == '__main__':
    app.run(debug=True)
