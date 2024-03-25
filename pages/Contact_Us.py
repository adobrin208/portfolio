import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    # adaugam text pe un singur rand
    user_email = st.text_input("Your email address")
    # adaugam text pe mai multe randuri
    message = st.text_area("Your message")
    # adaugam buton
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        print("Pressed!")
