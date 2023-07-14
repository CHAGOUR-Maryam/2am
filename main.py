import streamlit as st
from streamlit_option_menu import option_menu
from home import home
from email_sender import email
st.set_page_config(
    #page_icon=""",
    page_title='2am',
    layout="wide",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown("""
        <style>
               .block-container {
                    margin-top: 0rem;
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
    <style>
""", unsafe_allow_html=True)

selected = option_menu(None, ["Home", "Articles", "Tasks", 'Settings'],
    icons=['house', 'cloud-upload', "list-task", 'gear'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "white", "font-size": "25px"},
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "blue"},
    })
selected

if selected == "Home":
    home()
if selected == "Articles":
    email()
