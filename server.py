from flask import Flask
from flask import render_template
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
        if cipher == "caesar":
            caesar = encryption.CaesarCipher(key=key, message=message)
            encrypted_text = caesar.encrypt()
        elif cipher == "playfair":
            playfair = encryption.PlayfairCipher(key=key, message=message)
            encrypted_text = playfair.encrypt()
        return render_template('encrypt.html', message=message, cipher=cipher, key=key, en_text=encrypted_text)
    else:
        return render_template('encrypt.html', cipher='caesar')


@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == "POST":
        message = request.form.get("message")
        cipher = request.form.get("cipher")
        key = request.form.get("key")
        if cipher == "caesar":
            caesar = encryption.CaesarCipher(key=key, message=message)
            encrypted_text = caesar.decrypt()
        elif cipher == "playfair":
            playfair = encryption.PlayfairCipher(key=key, message=message)
            encrypted_text = playfair.decrypt()
        return render_template('decrypt.html', message=message, cipher=cipher, key=key, en_text=encrypted_text)
    else:
        return render_template('decrypt.html')
    


if __name__ == '__main__':
    app.run(debug=True)