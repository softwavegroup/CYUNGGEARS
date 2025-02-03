# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gear')
def gear():
    return render_template('gear.html')

@app.route('/Coffee')
def Coffee():
    return render_template('Coffee.html')

@app.route('/hiking')
def hiking():
    return render_template('hiking.html')

if __name__ == '__main__':
    app.run(debug=True)