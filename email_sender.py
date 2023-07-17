import streamlit as st
from PIL import Image

def email():
    st.header("How to create an interface for email automation with Streamlit-Python :")
    st.markdown("**Step 1:** Get your password from gmail:")
    with st.expander("**:blue[ Turn on 2 step verification]**"):
        st.markdown("**1.** Login to your Gmail account. In the upper-right corner, select your Image. From the menu, click on **Manage your Gmail account**.")
        im1=Image.open("pic1.png")
        st.image(im1)
        st.markdown("2. Click on the **Security** button in the left-hand sidebar.")
        im2=Image.open("pic2.png")
        st.image(im2)
        st.markdown("3. Click on **2-Step Verification** option.")
        im3=Image.open("pic3.png")
        st.image(im3)
        st.markdown("4. Navigate to the App Password option and tap on it.")
        im4=Image.open("pic4.png")
        st.image(im4)
        st.markdown("5. Select the app and device you want to generate the App password for:- Click the Generate button.")
        im5=Image.open("pic5.png")
        st.image(im5)
        st.markdown("6. A box appears with the password in it. Now you can copyapp password and use it.")
        #im6=Image.open("pic6.png")
        #st.image(im6)
    
    st.markdown("**Step2:** Create an interface for the email sender") 
