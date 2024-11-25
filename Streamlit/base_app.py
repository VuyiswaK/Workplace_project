"""
Simple Streamlit webserver application for serving developed classification
models.

Author: ExploreAI Academy.

Note:
---------------------------------------------------------------------
Please follow the instructions provided within the README.md file
located within this directory for guidance on how to use this script
correctly.
---------------------------------------------------------------------

Description: This file is used to launch a minimal streamlit web
application. You are expected to extend the functionality of this script
as part of your predict project.

For further help with the Streamlit framework, see:

https://docs.streamlit.io/en/latest/
"""

# Streamlit dependencies
import streamlit as st
import joblib
import os
import pandas as pd
import re
import requests
from io import BytesIO  # Import BytesIO
import numpy as np

# Function to fetch and load a pickle file from a URL
def load_pickle_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Use BytesIO to treat the bytes response as a file-like object
        return joblib.load(BytesIO(response.content))
    else:
        st.error(f"Error loading the file from URL: {url} (Status code: {response.status_code})")
        return None

# Vectorizer URL
#vectorizer_url = "https://raw.githubusercontent.com/VuyiswaK/2401PTDS_Classification_Project/main/Streamlit/tfidfvect.pkl"
#test_cv = load_pickle_from_url(vectorizer_url)

# Load your raw data
#raw = pd.read_csv('https://raw.githubusercontent.com/VuyiswaK/2401PTDS_Classification_Project/main/Streamlit/train.csv')


# The main function where we will build the actual app
def main():
    """Profit score Predictor"""

    st.title("Profit score")
    st.subheader("Predicting credit customer profit scores")

    options = ["Prediction", "Information"]
    selection = st.sidebar.selectbox("Choose Option", options)

    if selection == "Information":
        st.info("The predictor, is built to predict profit score, of clients using certain inputs.")
        st.markdown("""
            - Education
            - Technology
            - Business
            - Entertainment 
            - Sports
        """)

    if selection == "Prediction":
        st.info("Prediction with Random Forest Model")
        #st.image("https://raw.githubusercontent.com/VuyiswaK/2401PTDS_Classification_Project/main/Streamlit/science-in-the-news.png", use_column_width=True)
        
        # Creating a text box for user input
        Salary = st.number_input("Salary:", min_value=0, max_value=10000000, value=0)

        # Drop-down input box 
        option1 = np.array([*range(1,101)])/100
        Internal_PD = st.selectbox("Internal PD:", option1)

        option2 = np.array([*range(1,101)])/100
        External_PD = st.selectbox("External PD:", option2)

        Loan_amount = st.number_input("Loan Amount:", min_value=0, max_value=10000000, value=0)

        option3 = ['Yes','No']
        Banking_with_bank = st.selectbox("Banking with Bank:", option3)
        Banking_with_bank = 1 if Banking_with_bank == 'Yes' else 0

        option4 = np.array([*range(1,101)])/100
        Internal_utilisation = st.selectbox("Internal utilisation:", option4)

        option5 = np.array([*range(1,101)])/100
        External_utilisation = st.selectbox("External utilisation:", option5)

        option6 = np.array([*range(1,101)])/100
        Spend_percentage = st.selectbox("Spend percentage:", option6)

        #news_text = st.text_area("Enter news headline, content or description here", "Type Here")

        if st.button("Predict"):
            # Clean input text
            #cleaned_text = clean(news_text)
            
            # Transforming user input with vectorizer
            #vect_text = test_cv.transform([cleaned_text]).toarray()

            variables = np.array([Salary,
                                  Internal_PD,
                                  External_PD,
                                  Loan_amount,
                                  Banking_with_bank,
                                  Internal_utilisation,
                                  External_utilisation,
                                  Spend_percentage])

            # Load your model from the URL
            model_url = "https://raw.githubusercontent.com/VuyiswaK/2401PTDS_Classification_Project/main/Streamlit/prediction_model.pkl"
            predictor = load_pickle_from_url(model_url)
            
            if predictor is not None:
                prediction = predictor.predict(variables)
                st.success("Text Category: {}".format(prediction))

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
    main()


 