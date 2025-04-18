from flask import Flask # type: ignore
from flask import render_template # type: ignore
from flask import request
import encryption


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == "POST":
        message = request.form.get("message")
        cipher = request.form.get("cipher")
        key = request.form.get("key")
        cezar = encryption.CaesarCipher(key=key, message=message)
        encrypted_text = cezar.encrypt()
        return render_template('encrypt.html', message=message, cipher=cipher, key=key, en_text=encrypted_text)
    else:
        return render_template('encrypt.html')


@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == "POST":
        message = request.form.get("message")
        cipher = request.form.get("cipher")
        key = request.form.get("key")
        cezar = encryption.CaesarCipher(key=key, message=message)
        encrypted_text = cezar.decrypt()
        return render_template('decrypt.html', message=message, cipher=cipher, key=key, en_text=encrypted_text)
    else:
        return render_template('decrypt.html')
    


if __name__ == '__main__':
    app.run(debug=True)