from flask import Flask, render_template, url_for,flash, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from functools import wraps
from werkzeug.security import check_password_hash

from forms import RegistrationForm, LoginForm

# import mysql.connector
# from mysql.connector import Error
import json
import email_validator
from email_validator import validate_email, EmailNotValidError
import pandas as pd
import joblib
import xgboost
import psycopg2
from psycopg2 import sql, Error
from sklearn.preprocessing import LabelEncoder
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY']='a5cd36c715058bf2c9057169b7134a4d'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///siste.db'
# db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

db_config = {
    "host": "ep-crimson-block-a5wcgzxx.us-east-2.aws.neon.tech",
    "user":"neondb_owner",
    "password":"it1M9sTPAqEh",
    "database":"safe-mom",
    "port": 5432
}

#mysql connection
def get_db_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            host="ep-crimson-block-a5wcgzxx.us-east-2.aws.neon.tech",
            database="safe-mom",
            user="neondb_owner",
            password="it1M9sTPAqEh"
        )
        # connection = psycopg2.connect(**db_config)
        # if connection.is_connected():
        return connection
    except Error as e:
        print("Error: {e}")
    return connection

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login', next = request.url))
        return f(*args, **kwargs)
    return decorated_function

def redirect_home(f):
    @wraps(f)
    def decorated_home(*args, **kwargs):
        if 'user_id' in session:
            return redirect(url_for('hello_world'))
        return f(*args, **kwargs)
    return decorated_home


# @app.route("/", methods=['POST', 'GET'])
@app.route("/login", methods=['POST', 'GET'])
@redirect_home
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT id, password FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user[1], password):
            
            session['user_id'] = user[0]
            flash(f'Login successful! Welcome, {email}', 'success')
            # next_page = request.args.get('next')
            return redirect(url_for('hello_world'))

        else:
            print(f'Login Failed. Please check your email and password.', 'danger')

        cursor.close()
        connection.close()

    return render_template('login.html', title = 'Login', form = form)
    # if form.validate_on_submit():
    #     flash(f'Login Succesfull Welcome', 'success')
    #     return redirect(url_for('hello_world'))
    # return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out', "info")
    return redirect(url_for('login'))


@app.route("/register", methods=['POST', 'GET'])

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Validate the email of a user
        try:
            valid = validate_email(form.email.data)
            email = valid.email  # Extracts the normalized email if valid
        except EmailNotValidError as e:
            flash(str(e), 'danger')  #  if email is invalid
            return render_template('register.html', title='Register', form=form)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
         

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                       (form.username.data, form.email.data, hashed_password))
        connection.commit()
        cursor.close()
        connection.close()

        flash(f'Account Successfully Created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)



@app.route("/home",methods=["GET","POST"])
@login_required
def hello_world():
    return render_template('home.html')

@app.route("/about")
def jambo():
    return render_template('about.html', title='about')


@app.route("/contact")
def contact():
    return render_template("contact.html", title = "contact")


@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        print(to_predict_list)
        user_id = session.get('user_id')
        if not user_id:
            return "User Not logged in"

        connection = get_db_connection()
        cursor = connection.cursor()
        
        insert_query = '''
        INSERT INTO patients_data 
        (age, height, weight, bmi, sysbp, diabp, hb, pcv, platelet, creatinine, plgf_sflt, SEng, cysC, pp_13, glycerides, 
        htn, diabetes, fam_htn, sp_art, occupation, diet, activity, sleep, user_id) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (
            to_predict_list.get('age'),
            to_predict_list.get('height'),
            to_predict_list.get('weight'),
            to_predict_list.get('bmi'),
            to_predict_list.get('sysbp'),
            to_predict_list.get('diabp'),
            to_predict_list.get('hb'),
            to_predict_list.get('pcv'),
            to_predict_list.get('platelet'),
            to_predict_list.get('creatinine'),
            to_predict_list.get('plgf:sflt'),
            to_predict_list.get('SEng'),
            to_predict_list.get('cysC'),
            to_predict_list.get('pp_13'),
            to_predict_list.get('glycerides'),
            to_predict_list.get('htn'),
            to_predict_list.get('diabetes'),
            to_predict_list.get('fam_htn'),
            to_predict_list.get('sp_art'),
            to_predict_list.get('occupation'),
            to_predict_list.get('diet'),
            to_predict_list.get('activity'),
            to_predict_list.get('sleep'),
            user_id
        )
        
        cursor.execute(insert_query, values)
        
        connection.commit()

        cursor.close()
        connection.close()
        
        json_data = json.dumps(to_predict_list)
        
        # try:
        prediction, risk_percentage = preprocessDataAndPredict(json_data)
        return render_template('/predict.html', prediction = prediction, risk_percentage = risk_percentage)
         
        
        # except ValueError:
        #     return "Please Enter Valid Values"
        

    return "Method not allowed .."


def preprocessDataAndPredict(json_data):
    feature_dict = json.loads(json_data)
    test_data = {k: [v] for k, v in feature_dict.items()}
    test_data = pd.DataFrame(test_data)
    
    # Convert columns to appropriate numeric types
    cols_to_numeric = ['age', 'gest_age', 'height', 'weight', 'bmi', 'sysbp', 'diabp', 'hb',
       'pcv', 'tsh', 'platelet', 'creatinine', 'plgf:sflt', 'SEng', 'cysC',
       'pp_13', 'glycerides', 'htn', 'diabetes', 'fam_htn', 'sp_art',
       'occupation', 'diet', 'activity', 'sleep']

    for col in cols_to_numeric:
        test_data[col] = pd.to_numeric(test_data[col], errors='coerce')  # Converts non-numeric values to NaN

    
    if 'occupation' in test_data.columns:
    
        label_encoder = LabelEncoder()
        test_data['occupation'] = label_encoder.fit_transform(test_data['occupation'].astype(str))


    if 'next' in test_data.columns:
        test_data.drop('next', axis=1, inplace=True) 
    
    test_data.fillna(0, inplace=True)

    file = open("safe_mom_model_1.pkl", "rb")
    trained_model = joblib.load(file)
    
    prediction = trained_model.predict(test_data)
    risk_percentage = trained_model.predict_proba(test_data)[0][1] * 100  # Getting the probability of being at risk
    
    print(f"This is the prediction template: {prediction}")

    return prediction, risk_percentage



if __name__ == '__main__':
    app.run(debug=True)