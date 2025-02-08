[Data Science 2 Innovation Documentation](<https://github.com/SebbieMzingKe/Safe-Mom/blob/master/KamiLimu%20Research_%20Preeclampsia%20in%20Pregnant%20Women%20by%20Data%20Science%20Group%202.pdf>)

# Table of Contents


1. [Project Overview](#project-overview)
2. [Project Goals](#project-goals)
3. [Key Features](#key-features)
4. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Steps](#steps)
5. [Usage](#usage)
6. [License](#license)


# [Live Demo of Our Solution](<https://www.loom.com/share/eebbba9b6f164c009c2647f526a4d090>)

[![Watch the video](static/images/preeclampsia.png)](https://www.loom.com/share/90ed393ac43a4bf085f94dd308355164)


# Safe Mom: Predictive Machine Learning for Preeclampsia      

## **Project Overview:**  
Safe Mom is a predictive machine learning solution aimed at helping expectant mothers and healthcare professionals identify the likelihood of developing preeclampsia during the early stages of pregnancy. By leveraging patient data collected during the eighth week, the model provides valuable insights to mitigate risks and improve maternal health outcomes.

## **Project Goals:**
- *Predict early:* Identify the likelihood of preeclampsia at the eighth week of pregnancy.
- *Enhance care:* Empower healthcare providers to make informed decisions.
- *Improve outcomes:* Provide mothers with early intervention strategies for better health.

## *Key Features:*  
- *Machine Learning Model:* Utilizes advanced predictive algorithms to assess preeclampsia risk.  
- *Patient Data:*  Collects relevant health information.
- *User Interface:* Designed to be intuitive, ensuring easy input of patient data.

## Installation

### Prerequisites
- Python 3.x installed
- MySQL database set up
- `pip` for Python package installation

### Steps
1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/SebbieMzingKe/safe-mom.git
2. Navigate into the project directory.
   ```bash
   cd safe-mom
3. Set up a virtual environment.
   ```bash
   python -m venv env
   env\Scripts\activate  # On Mac, use `source env/bin/activate`
4. Install the dependencies from the requirements.txt file.
   ```bash
   pip install -r requirements.txt
5. Set up your MySQL database by importing the provided schema.
   ```bash
   psql postgresql://username:password@host/dbname # replace username, password, host and dbname with your's
6. Run the application.
   ```bash
   flask run or uvicorn app:app --reload or python app.py
7. If using docker
   ```bash
   docker pull sebbiemzing/safe-mom-web:latest
### Usage
On launching the Safe Mom, clinicians log in using their credentials. Once logged in, they can access the patient data input section.

Here, clinicians will enter patient vitals such as blood pressure, proteinuria, and fetal heart rate. Once the data is submitted, the machine learning model (powered by XGBoost) will process it.

The platform will then display the model's prediction on whether the patient is at risk of developing preeclampsia. Based on the results, the model will provide tailored recommendations, such as increasing monitoring, implementing preventive measures, or referring the patient to a specialist.  

## License
> Copyright 2024 Safe Mom

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated [documentation files](<[Data Science 2 Innovation Documentation](https://github.com/SebbieMzingKe/Safe-Mom/blob/master/KamiLimu%20Research_%20Preeclampsia%20in%20Pregnant%20Women%20by%20Data%20Science%20Group%202.pdf)>), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


