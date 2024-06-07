###############################################################################################
# Filename: Streamlit_component
# Owner: Shreyas Sawant
# Purpose of code: Following code handles the front-end part of the Socratic Tutor chatvot.
# Copyright (c) 2024 by Shreyas Sawant All Rights Reserved
# Last modified: 05-06-2024
###############################################################################################

import streamlit as st
import confidentiality_handler as conf
from cryptography.fernet import Fernet
from config import *

fernet = Fernet(ENCRYPTOR_KEY)

# Web Page configuration.
st.set_page_config(
    page_title = "Socratic tutor",
    page_icon = "💯",
    layout = "wide",
)

st.markdown(
    """
    # Socratic tutor AI chatbot
    #### By Shreyas Sawant \n
    
    This is a socratic tutor Chatbot which utilises the Llama3, gemma and mixtral AI models to generate chat output.
    By clicking the "Initiate tutor" button, the model will teach you about 
    the significance of actuators and sensors for Raspberry Pi.
    \n For more information, I recommend you to read the Description page.

    """
)

def main():
    with st.sidebar:
        select_model = st.selectbox(
                "Change model?",
                ("llama3-8b-8192", "gemma-7b-it", "mixtral-8x7b-32768")
            )
        st.write("Current model:", select_model)

    enc = conf.EncDecHandler()
    username = st.text_input("Enter your Username: ")
    dec_dict = enc.decode_dict_keys()

    if username in dec_dict:
        st.write("Press the below button if you want to forget the conversation and have a fresh start:")
        init_button = st.button("Initiate Tutor")
        #print("before:", conf.DATA_DICT)
        prompt_2 = st.chat_input("Say Something")
        name_index = enc.get_name_index(username, dec_dict)
    
        if prompt_2:
            result = enc.update_dict_data(username, prompt_2, initiate = False)
            #print("After:", conf.DATA_DICT)
            for i, key in enumerate(result.keys()):

                if i == name_index:
                    for m in range(len(result[key]['prompt'])):
                        for j in result[key]:
                            name_key = key
                            if j == "result":
                                st.success(result[key][j][m])
                            else:
                                st.write(result[key][j][m])

            st.success(result[name_key]["result"][-1])

        if init_button:
            result = enc.update_dict_data(username, query = None, initiate = True)
            for i, key in enumerate(result.keys()):
                if i == name_index:
                    st.success(result[key]["result"][0])
    
    elif username and username not in dec_dict: 
        st.success("Oops! looks like that username doesnt exist.")

if __name__ == '__main__':
    main()
