import streamlit as st
from PIL import Image

def email():
    st.header("How to create an interface for email automation with Streamlit-Python :")
    st.markdown("Step 1: get your password from gmail:")
    st.markdown("""First: Turn on 2 step verification
            1. Login to your Gmail account. In the upper-right corner, select your Image. From the menu, click on Manage your Gmail account.""")
    im1=Image.open("pic1.png")
    st.image(im1)
    st.markdown("2. Click on the Security button in the left-hand sidebar.")
    im2=Image.open("pic2.png")
    st.image(im2)
