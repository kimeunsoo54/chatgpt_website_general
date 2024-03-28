import streamlit as st
st.text('hello streamlit')

#홈페이지 꾸미기 
#html = 
#st.markdown(html, unsafe_allow_html=True)

member_name = ['김은수']
member_phone = ['01039109020']

# 리스트 요소 추가하는 함수 (새로운사람이 들어왔을 때)
# 따로 db를 만들자 (java script, html이 서로 호환됨)


def verification(name, phone):
  if member_name.index(name) == member_name.index(phone):

  if name not in member_name or phone not in member_phone:
    return "결제가 완료되지 않은 상태입니다"


