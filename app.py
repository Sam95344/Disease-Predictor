
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

app = Flask(__name__)

# Load the datasets
df = pd.read_csv("Training.csv")
tr = pd.read_csv("Testing.csv")

# Define the list of symptoms and diseases
l1 = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
      'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
      'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
      'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
      'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
      'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
      'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
      'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
      'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
      'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
      'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
      'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
      'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
      'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
      'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
      'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
      'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
      'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
      'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
      'yellow_crust_ooze']

disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
           'Peptic ulcer disease', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
           'Migraine', 'Cervical spondylosis',
           'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'Hepatitis A',
           'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
           'Common Cold', 'Pneumonia', 'Dimorphic hemorrhoids (piles)',
           'Heart attack', 'Varicose veins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthritis',
           'Arthritis', '(vertigo) Paroxysmal Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis',
           'Impetigo']

# Prepare the training data
df['prognosis'] = df['prognosis'].astype('category').cat.codes  # Convert disease names to numeric codes
X = df[l1]
y = df['prognosis']

# Prepare the testing data
tr['prognosis'] = tr['prognosis'].astype('category').cat.codes  # Convert disease names to numeric codes
X_test = tr[l1]
y_test = tr['prognosis']

# Define the model class
class Model:
    def __init__(self):
        self.clf_tree = tree.DecisionTreeClassifier().fit(X, y)
        # self.clf_forest = RandomForestClassifier().fit(X, y)
        # self.gnb = GaussianNB().fit(X, y)

    def predict(self, symptoms):
        l2 = [0] * len(l1)
        for symptom in symptoms:
            if symptom in l1:
                l2[l1.index(symptom)] = 1

        input_data = [l2]
        tree_prediction = self.clf_tree.predict(input_data)[0]
        # forest_prediction = self.clf_forest.predict(input_data)[0]
        # gnb_prediction = self.gnb.predict(input_data)[0]

        return {
            "decision_tree": disease[tree_prediction],
            # "random_forest": disease[forest_prediction],
            # "naive_bayes": disease[gnb_prediction],
        }

model = Model()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symptoms = [
            request.form.get('symptom1'),
            request.form.get('symptom2'),
            request.form.get('symptom3'),
            request.form.get('symptom4'),
            request.form.get('symptom5')
        ]
        predictions = model.predict(symptoms)
        return render_template('index.html', predictions=predictions, symptoms=l1)  # Pass symptoms to the template

    return render_template('index.html', predictions=None, symptoms=l1)  # Pass symptoms to the template

if __name__ == "__main__":
    app.run(debug=True)
