from flask import Flask # type: ignore
from flask import render_template # type: ignore
from flask import request
import encryption


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form.get("message")
    cipher = request.form.get("cipher")
    key = request.form.get("key")
    return render_template('encrypt.html', message=message, cipher=cipher, key=key)


if __name__ == '__main__':
    app.run(debug=True)