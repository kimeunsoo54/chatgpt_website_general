import streamlit as st
import time


#홈페이지 꾸미기
#html = 
#st.markdown(html, unsafe_allow_html=True)

#페이지 분리 (같은 repository 내 다른 파일을 생성하고 st.page_link로 연결)



# 따로 csv DB를 만들자





'''
세특 gpt 본격적으로 사용하기 - langchain 이용
def generate_seteuk() :
  ~~~~ 랭체인 챗지피티 작동 ~~~~
'''


'''
def freetrial():
  while True:
    if csv에서 남은 횟수 == 0:
      print("무료 이용 횟수를 초과하였습니다. 3초 후 종료됩니다.")
      time.sleep(3)
      break
    
    generate_seteuk()
    #csv에서 number -1
'''
    
  
  



def signup():
  name_student = st.text_input("학생 성함을 입력해주세요")
  phone_student = st.text_input("학생 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)")
  name_parent = st.text_input("학부모님 성함을 입력해주세요")
  phone_parent = st.text_input("학부모님 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)")
  id = st.text_input("아이디를 입력해주세요")
  password = st.text_input("비밀번호를 입력해주세요")
  password_check = st.text_input("비밀번호를 한 번 더 입력해주세요")
  

  #csv 파일에 이미 있는 사람이면 재가입 못하도록 접근 막아야 한다 (학생, 학부모 정보로 판단)
  '''
  if password == password_check:
    #csv 파일에 명단 추가 (사용 횟수를 세기 위한 숫자 3도 같이 입력)
    #로그인 페이지로 이동
  else:
    print("비밀번호가 일치하지 않습니다")
    def signup()
  '''


def login():
  id = st.text_input("아이디")
  password = st.text_input("비밀번호")

  
  #csv 파일 자료와 일치하면 무료체험 버튼 클릭하게 하기
    #button_freetrial = st.button('3회 무료체험')
    #button.on_click(freetrial)




'''
def logout():
  st.page_link("signup, login 화면으로 이동")
'''




button_signup = st.button('회원가입')
button_longin = st.button('로그인')

button_signup.on_click(signup)
button_login.on_click(login)


  
  
  
  











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

