import streamlit as st

def login():
    with st.form("form2", clear_on_submit = True):
        id = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")

        submit = st.form_submit_button("로그인")

login()
