from flask import Flask, render_template, url_for,flash, redirect
from forms import RegistrationForm, LoginForm
import email_validator

app = Flask(__name__)
app.config['SECRET_KEY']='a5cd36c715058bf2c9057169b7134a4d'


@app.route("/", methods=['POST', 'GET'])
@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login Succesfull Welcome', 'success')
        return redirect(url_for('hello_world'))
    return render_template('login.html', title='Login', form=form)

@app.route("/home")
def hello_world():
    return render_template('home.html')

@app.route("/about")
def jambo():
    return render_template('about.html', title='about')

@app.route("/register", methods=['POST', 'GET'])

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Acount Successfully Created For {form.username.data }!', 'success')
        return redirect(url_for('hello_world'))
    return render_template('register.html', title='Register', form=form)




if __name__ == '__main__':
    app.run(debug=True)
