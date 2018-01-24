from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'amrish'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!',
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!',
        },
        {
            'author': {'username': 'Simon'},
            'body': 'I like cheese',
        },
        {
            'author': {'username': 'Jess'},
            'body': 'I want to go to the park',
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
