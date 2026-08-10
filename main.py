import os
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Multiple Disease Prediction", layout="wide", page_icon="⚕️")

# Loading the saved models
# Ensure these .sav files are in the same directory as your script
diabetes_model = pickle.load(open('diabetes_trained_model.sav', 'rb'))
heart_model = pickle.load(open('heart_disease_trained_model.sav', 'rb'))
parkinsons_model = pickle.load(open('Parkinsson_disease_trained_model.sav', 'rb'))

# Sidebar for navigation using native Streamlit radio buttons
with st.sidebar:
    st.title('Disease Prediction System')
    selection = st.radio(
        'Select a Disease to Predict:',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsson Disease Prediction']
    )

# ==========================================
# Diabetes Prediction Page
# ==========================================
if selection == 'Diabetes Prediction':
    
    st.title('Diabetes Prediction Using ML (SVM Model)')
    
    # Getting the input data from user
    c1, c2, c3 = st.columns(3)
    
    with c1:
        Pregnancies = st.text_input('Number of Pregnancies', value="0")
    with c2:
        Glucose = st.text_input('Glucose Level', value="0")
    with c3:
        BloodPressure = st.text_input('Blood Pressure Value', value="0")
    with c1:
        SkinThickness = st.text_input('Skin Thickness Value', value="0")
    with c2:
        Insulin = st.text_input('Insulin Level', value="0")
    with c3:
        BMI = st.text_input('BMI Value', value="0")
    with c1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value', value="0")
    with c2:
        Age = st.text_input('Age of person', value="0")
         
    # Code for prediction
    dia_diagnosis = ''
    
    # Creating a button 
    if st.button('Diabetes Test Result'):
        try:
            # Convert string inputs to floats before prediction
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            user_input = [float(x) for x in user_input]
            
            dia_pred = diabetes_model.predict([user_input])
            
            if dia_pred[0] == 1:
                dia_diagnosis = "The Person is Diabetic"
            else:
                dia_diagnosis = "The Person is not Diabetic"
                
            st.success(dia_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")

# ==========================================
# Heart Disease Prediction Page
# ==========================================
if selection == 'Heart Disease Prediction':
    
    st.title('Heart Disease Prediction Using ML (Logistic Regression Model)')
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        age = st.text_input('Age of Person', value="0")
    with c2:
        sex1 = st.selectbox('Sex of Person', options=['Male', 'Female'])
        sex = 1 if sex1 == 'Male' else 0
    with c3:
        cp = st.text_input('Chest Pain Type (0/1/2/3)', value="0")
    with c1:
        trestbps = st.text_input('Resting Blood Pressure', value="0")
    with c2:
        chol = st.text_input('Serum Cholestroal in mg/dl', value="0")
    with c3:
        fbs1 = st.text_input('Fasting Blood Sugar > 120 mg/dl', value="0")
        fbs = 1 if float(fbs1) > 120 else 0
    with c1:
        restecg = st.text_input('Resting Electrocardiographic (0/1)', value="0")
    with c2:
        thalach = st.text_input('Maximum Heart Rate achieved', value="0")
    with c3:
        exang1 = st.selectbox('Exercise Induced Angina', options=['Yes', 'No'])
        exang = 1 if exang1 == 'Yes' else 0
    with c1:
        oldpeak = st.text_input('ST depression induced by Exercise', value="0")
    with c2:
        slope = st.text_input('Slope of the peak exercise ST segment', value="0")
    with c3:
        ca = st.text_input('No. of Major vessels (0-3) colored by flourosopy', value="0")
    with c1:
        thal = st.text_input('thal: 0=Normal; 1=Fixed defect; 2=Reversable defect', value="0")
        
    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]

            heart_prediction = heart_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

            st.success(heart_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")

# ==========================================
# Parkinson's Disease Prediction Page
# ==========================================
if selection == 'Parkinsson Disease Prediction':
    
    st.title("Parkinson's Disease Prediction Using ML (SVM Model)")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', value="0")
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', value="0")
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', value="0")
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', value="0")
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', value="0")
    with col1:
        RAP = st.text_input('MDVP:RAP', value="0")
    with col2:
        PPQ = st.text_input('MDVP:PPQ', value="0")
    with col3:
        DDP = st.text_input('Jitter:DDP', value="0")
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer', value="0")
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', value="0")
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3', value="0")
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5', value="0")
    with col3:
        APQ = st.text_input('MDVP:APQ', value="0")
    with col4:
        DDA = st.text_input('Shimmer:DDA', value="0")
    with col5:
        NHR = st.text_input('NHR', value="0")
    with col1:
        HNR = st.text_input('HNR', value="0")
    with col2:
        RPDE = st.text_input('RPDE', value="0")
    with col3:
        DFA = st.text_input('DFA', value="0")
    with col4:
        spread1 = st.text_input('spread1', value="0")
    with col5:
        spread2 = st.text_input('spread2', value="0")
    with col1:
        D2 = st.text_input('D2', value="0")
    with col2:
        PPE = st.text_input('PPE', value="0")

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        try:
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                          RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                          APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

            user_input = [float(x) for x in user_input]

            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

            st.success(parkinsons_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")
