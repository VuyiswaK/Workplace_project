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
import streamlit as st
import requests
from io import BytesIO
from PIL import Image


# Set your token as an environment variable
os.environ['GITHUB_TOKEN'] = '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'

# Access the token in your app
token = os.getenv('GITHUB_TOKEN')


# Images
ps1 = 'https://raw.githubusercontent.com/VuyiswaK/Workplace_project/main/Streamlit/ps1.jpg'
ps2 = 'https://raw.githubusercontent.com/VuyiswaK/Workplace_project/main/Streamlit/ps2.png'
ps3 = 'https://raw.githubusercontent.com/VuyiswaK/Workplace_project/main/Streamlit/ps3.jpeg'
ps4 = 'https://raw.githubusercontent.com/VuyiswaK/Workplace_project/main/Streamlit/ps4.jpg'
ps5 = 'https://raw.githubusercontent.com/VuyiswaK/Workplace_project/main/Streamlit/ps5.jpg'
ps6 = 'https://raw.githubusercontent.com/VuyiswaK/Workplace_project/main/Streamlit/ps6.jpg'
ps789 = 'https://raw.githubusercontent.com/VuyiswaK/Workplace_project/main/Streamlit/ps789.jpg'
ps10 = 'https://raw.githubusercontent.com/VuyiswaK/Workplace_project/main/Streamlit/ps10.png'

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

# Function to fetch and load an image from a URL using a token
def load_image_from_url(url, token):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Use BytesIO to treat the bytes response as a file-like object
        return Image.open(BytesIO(response.content))
    else:
        st.error(f"Error loading the image from URL: {url} (Status code: {response.status_code})")
        return None

# The main function where we will build the actual app
def main():
    """Profit score Predictor"""

    st.title("Profit scoring")
    st.subheader("Predicting profit scores of debtors")

    options = ["Prediction", "Information"]
    selection = st.sidebar.selectbox("Choose Option", options)

    if selection == "Information":
        st.info("The predictor, using a random forest classifier to predict profit scores of a client using certain portfolio inputs.")
        st.markdown("""
            - Salary
            - Internal PD: Probability of default computed internally 
            - External PD: Probability of default computed externally
            - Loan amount: The size of the loan taken out
            - Baking with bank: Whether they bank with the same back they have credit with
            - Internal utilisation: Utilisation of the credit with the bank
            - External utiloisation: Utilistaion with credit taken out with other institutions
            - Spend percentage: Amount transacted in the given month
        """)

    if selection == "Prediction":
        st.info("Select or input the appropriate values for a particular client and press the predict button to see what their profit score is.")
        
        # Creating a text box for user input
        col1, col2 = st.columns([1, 3])
        with col1: 
            st.markdown("<p style='font-size:20px;'>Salary:</p>", unsafe_allow_html=True)
        with col2: 
            Salary = st.number_input("", min_value=0, max_value=10000000, value=0, key="salary")

        # INTERNAL PD
        option1 = np.array([*range(1,101)])/100
        col1, col2 = st.columns([1, 3])
        with col1: 
            st.markdown("<p style='font-size:20px;'>Internal PD:</p>", unsafe_allow_html=True)
        with col2: 
            Internal_PD = st.selectbox("", option1, key="internal_pd")

        # EXTERNAL PD
        option2 = np.array([*range(1,101)])/100
        col1, col2 = st.columns([1, 3])
        with col1: 
            st.markdown("<p style='font-size:20px;'>External PD:</p>", unsafe_allow_html=True)
        with col2: 
            External_PD = st.selectbox("", option2, key="external_pd")

        # LOAN AMOUNT
        col1, col2 = st.columns([1, 3])
        with col1: 
            st.markdown("<p style='font-size:20px;'>Loan Amount:</p>", unsafe_allow_html=True)
        with col2: 
            Loan_amount = st.number_input("", min_value=0, max_value=10000000, value=0, key="loan_amount")

        # BANKING WITH BANK
        option3 = ['Yes','No']
        col1, col2 = st.columns([1, 3])
        with col1: 
            st.markdown("<p style='font-size:20px;'>Banking with Bank:</p>", unsafe_allow_html=True)
        with col2: 
            Banking_with_bank = st.selectbox("", option3, key="banking_with_bank")
        Banking_with_bank = 1 if Banking_with_bank == 'Yes' else 0

        # INTERNAL UTILISATION
        option4 = np.array([*range(1,101)])/100
        col1, col2 = st.columns([1, 3])
        with col1: 
            st.markdown("<p style='font-size:20px;'>Internal utilisation:</p>", unsafe_allow_html=True)
        with col2: 
            Internal_utilisation = st.selectbox("", option4, key="internal_utilisation")

        # EXTERNAL UTILISATION
        option5 = np.array([*range(1,101)])/100
        col1, col2 = st.columns([1, 3])
        with col1: 
            st.markdown("<p style='font-size:20px;'>External utilisation:</p>", unsafe_allow_html=True)
        with col2: 
            External_utilisation = st.selectbox("", option5, key="external_utilisation")

        # SPEND PERCENTAGE
        option6 = np.array([*range(1,101)])/100
        col1, col2 = st.columns([1, 3])
        with col1: 
            st.markdown("<p style='font-size:20px;'>Spend percentage:</p>", unsafe_allow_html=True)
        with col2: 
            Spend_percentage = st.selectbox("", option6, key="spend_percentage")

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
                st.success(f"Profit score: {int(prediction[0])}")
                if int(prediction[0]) == 1:
                    image_url = ps1
                    text = 'You are in the red zone and most likely to default. It may that you can no longer afford to finance the debt. Worry not there are ways to resolve this if you reach out to us, but please be swift.'
                elif int(prediction[0]) == 2:
                    image_url = ps2
                    text = 'You are willing to pay down the debt but are financial stretched with all the other credit cards, contact us so we can guide you on the way forward to avoid the red zone. '
                elif int(prediction[0]) == 3:
                    image_url = ps3
                    text = 'You are one of our oldest customers. Thank you for the loyalty, but your spending and utilisation of the card seems to have decreased overtime. Let us know how we can encourage you to use your card more as that is what the credit card is for'
                elif int(prediction[0]) == 4:
                    image_url = ps4
                    text = 'Penny pincher hey, spend more to move from negative to positive profitability,'
                elif int(prediction[0]) == 5:
                    image_url = ps5
                    text = "Congratulations, you make up the profitability of majority of our customers, but don't be complacent you can rise above the norm"
                elif int(prediction[0]) == 6:
                    image_url = ps6
                    text = 'You are above the average profitability, keep it up.'
                elif int(prediction[0]) == 10:
                    image_url = ps10
                    text = 'You are indeed the cherry on top, the top 0.05% of our profitable clients. You overachiever, how do you do it !'
                else:
                    image_url = ps789
                    text = 'Well done, you are a reasonably profitable client. We may just reward you for this type of behaviour'
                               
                # Display image and text side by side
                col1, col2, = st.columns([2, 2])
                
                with col1:
                    st.image(load_image_from_url(image_url, token), width=200)  # Adjust width as needed
                
                with col2:
                    st.markdown(f"<p style='font-size:20px;'>{text}</p>", unsafe_allow_html=True)
                
# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
    main()
