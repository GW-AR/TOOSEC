
from flask import Flask
from flask import render_template
from flask import request
import url_class

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/url', methods=['GET', 'POST'])
def url():

    if request.method == 'GET':
        page = url_class.Url("")
        return render_template('url.html', page_object=page)

    elif request.method == 'POST':

        page = url_class.Url(request.form['link_url'])
        page.check_url_address()
        return render_template('url.html', page_object=page)

if __name__ == '__main__':
    app.run(debug=True)