from flask import Flask
from flask import render_template
from flask import request
import password


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generator', methods=['GET', 'POST'])
def password_generator():

    if request.method == 'GET':
        password_object = password.Password(12,"on", "on", 1,"on",1)
        return render_template('password.html', password_options=password_object)
    
    elif request.method == 'POST':

        password_object = password.Password(
            request.form.get('length'),
            request.form.get('contain_uppercase'),
            request.form.get('contain_characters'),
            request.form.get('min_special_char'),
            request.form.get('contain_numbers'),
            request.form.get('min_numbers'),
        )

        # print(f'Length: {password_object.length}')
        # print(f'Contain_upper_case: {password_object.contain_uppercase}')
        # print(f'Contain_char: {password_object.contain_char}')
        # print(f'Min_char: {password_object.min_special_char}')
        # print(f'Contain_numbers: {password_object.contain_numbers}')
        # print(f'Min_numbers: {password_object.min_numbers}')

        generated_password = password_object.generate_password()

        return render_template('password.html', generated_password=generated_password, password_options=password_object)



if __name__ == '__main__':
    app.run(debug=True)