import streamlit as st

st.set_page_config(
    page_title = "회원가입",
    page_icon = "👋"
)

def signup():
    with st.form("form1", clear_on_submit = True):
        name_student = st.text_input("학생 성함을 입력해주세요", key=1)
        phone_student = st.text_input("학생 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)", key=2)
        name_parent = st.text_input("학부모님 성함을 입력해주세요", key=3)
        phone_parent = st.text_input("학부모님 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)", key=4)
        id = st.text_input("아이디를 입력해주세요", key=5)
        password = st.text_input("비밀번호를 입력해주세요. 정확히 입력했는지 반드시 확인 바랍니다.", key=6, type="password")

        submit = st.form_submit_button("작성 완료")
        
signup()