import streamlit as st
import time
from signup_page import signup


#홈페이지 꾸미기
#html = 
#st.markdown(html, unsafe_allow_html=True)

#페이지 분리 (같은 repository 내 다른 파일을 생성하고 st.page_link로 연결)
# 따로 csv DB를 만들자
  



def signup():
    with st.form("form1", clear_on_submit = True):
        name_student = st.text_input("학생 성함을 입력해주세요", key=1)
        phone_student = st.text_input("학생 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)", key=2)
        name_parent = st.text_input("학부모님 성함을 입력해주세요", key=3)
        phone_parent = st.text_input("학부모님 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)", key=4)
        id = st.text_input("아이디를 입력해주세요", key=5)
        password = st.text_input("비밀번호를 입력해주세요. 정확히 입력했는지 반드시 확인 바랍니다.", key=6, type="password")

        submit = st.form_submit_button("작성 완료")




def login():
    with st.form("form2", clear_on_submit = True):
        id = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")

        submit = st.form_submit_button("로그인")




page_names_to_funcs = {
    "회원가입":signup,
    "로그인": login
}



page_name = st.sidebar.selectbox("회원가입, 로그인 중 하나를 선택하세요", page_names_to_funcs.keys())
page_names_to_funcs[page_name]()








if st.button("회원가입"):
    st.page_link("pages/signup_page")

                 
#csv 파일에 이미 있는 사람이면 재가입 못하도록 접근 막아야 한다 (학생, 학부모 정보로 판단)
#csv 파일에 명단 추가 (사용 횟수를 세기 위한 숫자 3도 같이 입력)
#로그인 페이지로 이동


if st.button("로그인"):
    login()
    



  
"""
#세특 gpt 본격적으로 사용하기 - langchain 이용
def generate_seteuk() :
  ~~~~ 랭체인 챗지피티 작동 ~~~~




def freetrial():
  while True:
    if csv에서 남은 횟수 == 0:
      #에러띄우기 "무료 이용 횟수를 초과하였습니다. 3초 후 종료됩니다.")
      time.sleep(3)
      break
    
    generate_seteuk()
    #csv에서 number -1

"""




  
  











'''
# payment 도입 이후 본인인증
def verification_subscription(name, phone):
  name_student = st.text_input("학생 성함을 입력해주세요")
  phone_student = st.text_input("학생 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)")
  
  if member_name_paid.index(name) == member_phone_paid.index(phone):
    #generate_seteuk()

  if name not in member_name_paid or phone not in member_phone_paid:
    st.error("구매자 명단에 사용자님의 정보가 없습니다.")
'''

