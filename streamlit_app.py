###############################################################################################
# Filename: Streamlit_component
# Owner: Shreyas Sawant
# Purpose of code: Following code handles the front-end part of the Socratic Tutor chatvot.
# Copyright (c) 2024 by Shreyas Sawant All Rights Reserved
# Last modified: 04-06-2024
###############################################################################################

import confidentiality_handler as conf
import streamlit as st
from config import *

# Web Page configuration.
st.set_page_config(
    page_title = "Socratic tutor",
    page_icon = "💯",
    layout = "wide",
)

st.markdown(
    """
    # Welcome to the Socratic tutor AI chatbot!
    #### By Shreyas Sawant \n
    
    \n For more information, I recommend you to read the Description page.
    """
)

def main():
    st.write("Is this your first time using the app?")

    col1, col2, col3, col4 = st.columns(4)
    yes_button = col2.button("Yes!")
    no_button = col3.button("No, this is my first time")

    if yes_button:
        st.write("Great! Well then continue on in the chatbot page")

    elif no_button:
        st.write("Ok, then start off by entering a preferable username")
    
    username = st.text_input("Enter your username")
    st.write("Note: I recommend to not use your actual name 😁")

    if username:
        enc = conf.EncDecHandler()
        if username not in enc.decode_dict_keys():
            enc_name = enc.encryptor(username)
            enc.update_dict(enc_name)
            st.success("YOU ARE ALL SET!! ENJOY THE CHATTING EXPERIENCE!")
        
        else:
            st.success("HEYYY! THAT NAME ALREADY EXISTS 🤨; CHOOSE ANOTHER ONE")

if __name__ == '__main__':
    main()