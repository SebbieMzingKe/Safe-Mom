from flask import Flask, render_template, url_for,flash, redirect, request
from forms import RegistrationForm, LoginForm
import email_validator
import pandas as pd
import joblib
import xgboost
import numpy as np

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

@app.route("/home",methods=["GET","POST"])
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



# Load the model 
file = open("safe_mom_model_1.pkl", "rb")
model = joblib.load(file)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Collect form data
        form_data = {
            'age': request.form.get('age'),
            'gestational': request.form.get('gestational'),
            'height': request.form.get('height'),
            'weight': request.form.get('pregnancies'),
            'bmi': request.form.get('bmi'),
            'sysBP': request.form.get('sysBP'),
            'dysBP': request.form.get('dysBP'),
            'hb': request.form.get('hb'),
            'pcv': request.form.get('pcv'),
            'tsh': request.form.get('tsh'),
            'platelet': request.form.get('platelet'),
            'creatinine': request.form.get('creatinine'),
            'plgf_sflt': request.form.get('plgf:sflt'),
            'SEeng': request.form.get('SEeng'),
            'cysC': request.form.get('cysC'),
            'pp_13': request.form.get('pp_13'),
            'glycerides': request.form.get('glycerides'),
            'Hypertension': request.form.get('Hypertension'),
            'diabetes': request.form.get('diabetes'),
            'fam_htn': request.form.get('fam_htn'),
            'sp_art': request.form.get('sp_art'),
            'occupation': request.form.get('occupation'),
            'diet': request.form.get('diet'),
            'activity': request.form.get('activity'),
            'sleep': request.form.get('sleep')
        }

        # Convert form data into a list of values
        input_data = list(form_data.values())

        # Convert the input data to a numpy array
        data_numpy = np.array(input_data, dtype=float)

        # Reshape the array for a single prediction
        data_reshaped = data_numpy.reshape(1, -1)

        # Make the prediction
        prediction = model.predict(data_reshaped)

        # Render the results template with the prediction
        return render_template('predict.html', prediction=prediction)

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
