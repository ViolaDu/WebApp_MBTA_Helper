"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from src.mbta_helper import find_stop_near
app = Flask(__name__)

app.config['DEBUG'] = True
app.secret_key = "Some secret string here"

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/station/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        a = request.form['a']

        root_1, root_2 = find_stop_near(a)

        if root_1:
            return render_template('Result.html', a=a,
                                   root_1=root_1, root_2=root_2)
        else:
            return render_template('form.html', error=True)
    return render_template('form.html', error=None)



if __name__ == '__main__':
    app.run()
