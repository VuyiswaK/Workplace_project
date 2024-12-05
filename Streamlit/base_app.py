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

import streamlit as st
import joblib
import os
import pandas as pd
import re
import requests
from io import BytesIO  # Import BytesIO
import numpy as np
import requests
import base64
import pickle

images

# Function to fetch and load a pickle file from a URL
def load_pickle_from_url(url, token):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Use BytesIO to treat the bytes response as a file-like object
        return joblib.load(BytesIO(response.content))
    else:
        st.error(f"Error loading the file from URL: {url} (Status code: {response.status_code})")
        return None

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

        if st.button("Predict"):
            variables = np.array([Salary,
                                  Internal_PD,
                                  External_PD,
                                  Loan_amount,
                                  Banking_with_bank,
                                  Internal_utilisation,
                                  External_utilisation,
                                  Spend_percentage])

            # Replace with your GitHub personal access token
            token = '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'
            # Use the raw URL for the pickle file
            model_url = 'https://raw.githubusercontent.com/VuyiswaK/Workplace_project/main/Streamlit/prediction_model.pkl'

            model = load_pickle_from_url(model_url, token)
            
            if model is not None:
                prediction = model.predict([variables])
                #st.success(f"Text Category: {int(prediction[0])}")
                if int(prediction[0]) == 1:
                    image_url = "https://example.com/path/to/your/image.jpg" # Display image and text side by side col1, col2 = st.columns([1, 3]) with col1: st.image(image_url, width=100) # Adjust width as needed with col2: st.write("This is the text next to the image. You can add more details here.") # Additional content st.write("More content below the image and text."

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
    main()
