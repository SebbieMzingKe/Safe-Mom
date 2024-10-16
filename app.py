from flask import Flask, render_template, url_for,flash, redirect, request
from forms import RegistrationForm, LoginForm
import email_validator
import pandas as pd
import joblib
import xgboost

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

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()

        try:
            prediction = preprocessDataAndPredict(to_predict_list)
            return render_template('/predict.html', prediction = prediction)
        
        except ValueError:
            return "Please Enter Valid Values"
        

    return "Method not allowed"

def preprocessDataAndPredict(feature_dict):
    test_data = {k:[v] for k, v in feature_dict.items()}
    test_data = pd.DataFrame(test_data) 
    
    file = open("safe_mom_model_1.pkl", "rb")
    
    trained_model = joblib.load(file)
    
    predict = trained_model.predict(test_data)

    return predict


if __name__ == '__main__':
    app.run(debug=True)
