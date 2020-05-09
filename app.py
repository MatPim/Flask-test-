from flask import Flask, render_template

app = Flask(__name__)
title = 'Hello World'
alou = 'Bla Bla'
@app.route('/')

def index():
    return(render_template('index.html', title = title))

@app.route('/bla')
def bla():
    return(render_template('index.html', title = alou))