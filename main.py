import streamlit as st
import time


#홈페이지 꾸미기
#html = 
#st.markdown(html, unsafe_allow_html=True)

#페이지 분리 (같은 repository 내 다른 파일을 생성하고 st.page_link로 연결)
# 따로 csv DB를 만들자





if st.button("회원가입"):
    st.switch_page("pages/signup_page.py")

                 
#csv 파일에 이미 있는 사람이면 재가입 못하도록 접근 막아야 한다 (학생, 학부모 정보로 판단)
#csv 파일에 명단 추가 (사용 횟수를 세기 위한 숫자 3도 같이 입력)
#로그인 페이지로 이동


if st.button("로그인"):
    st.switch_page("pages/login_page.py")
