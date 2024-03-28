import streamlit as st
import time


#홈페이지 꾸미기
#html = 
#st.markdown(html, unsafe_allow_html=True)

#페이지 분리 (같은 repository 내 다른 파일을 생성하고 st.page_link로 연결)



# 따로 csv DB를 만들자






    
  




def signup():
  name_student = st.text_input("학생 성함을 입력해주세요", key=1)
  st.write(name_student)
  phone_student = st.text_input("학생 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)", key=2)
  st.write(phone_student)
  name_parent = st.text_input("학부모님 성함을 입력해주세요", key=3)
  st.write(name_parent)
  phone_parent = st.text_input("학부모님 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)", key=4)
  st.write(phone_parent)
  id = st.text_input("아이디를 입력해주세요", key=5)
  st.write(id)
  password = st.text_input("비밀번호를 입력해주세요", key=6, type="password")
  st.write(len(password), "글자의 비밀번호입니다")
  password_check = st.text_input("비밀번호를 한 번 더 입력해주세요", key=7)
  st.write(len(password_check), "글자의 비밀번호입니다")


  if st.button("완료"):
      if password == password_check:
          st.write("done")
  


  


def login():
  id = st.text_input("아이디")
  st.write(id)
  password = st.text_input("비밀번호", type="password")
  st.write(len(password), "글자입니다")

  













if st.button("회원가입"):
    with st.form("form1", clear_on_submit = True):
    name_student = st.text_input("학생 성함을 입력해주세요", key=1)
    phone_student = st.text_input("학생 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)", key=2)
    name_parent = st.text_input("학부모님 성함을 입력해주세요", key=3)
    phone_parent = st.text_input("학부모님 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)", key=4)
    id = st.text_input("아이디를 입력해주세요", key=5)
    password = st.text_input("비밀번호를 입력해주세요", key=6, type="password")
    password_check = st.text_input("비밀번호를 한 번 더 입력해주세요", key=7)

    submit = st.form_submit_button("작성 완료")

if st.button("로그인"):
    login()



  
  
  
  











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

