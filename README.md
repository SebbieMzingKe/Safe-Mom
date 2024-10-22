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
   mysql -u username -p safe-mom < safe-mom.sql

6. Run the application.
   ```bash
   flask run or uvicorn app:app --reload or python app.py
### Usage
On launching the Safe Mom, clinicians log in using their credentials. Once logged in, they can access the patient data input section.

Here, clinicians will enter patient vitals such as blood pressure, proteinuria, and fetal heart rate. Once the data is submitted, the machine learning model (powered by XGBoost) will process it.

The platform will then display the model's prediction on whether the patient is at risk of developing preeclampsia. Based on the results, the model will provide tailored recommendations, such as increasing monitoring, implementing preventive measures, or referring the patient to a specialist.
