import streamlit as st
import csv





def signup():
	
	"""
	if 'id' not in st.session_state:
		st.session_state['id']=''

	if 'pw' not in st.session_state:
		st.session_state['pw']=''

	if 'number' not in st.session_state:
		st.session_state['number']=''
		
	if 'name_student' not in st.session_state:
    		st.session_state['name_student'] = ''
		
	if 'phone_student' not in st.session_state:
    		st.session_state['phone_student'] = ''
	"""
	
	
	with st.form("form1", clear_on_submit = False):
		

		
		name_student = st.text_input("학생 성함을 입력해주세요", key=1)
		#if name_student:
			#st.session_state['name_student'] = name_student
		
		phone_student = st.text_input("학생 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)", key=2)
		#if phone_student:
			#st.session_state['phone_student'] = phone_student
		
		name_parent = st.text_input("학부모님 성함을 입력해주세요", key=3)
		phone_parent = st.text_input("학부모님 전화번호를 입력해주세요 (띄어쓰기, 하이픈(-) 제외하고 숫자만)", key=4)
		id = st.text_input("아이디를 입력해주세요", key=5)
		password = st.text_input("비밀번호를 입력해주세요. 정확히 입력했는지 반드시 확인 바랍니다.", key=6, type="password")

		submit = st.form_submit_button("작성 완료")

		if submit == True:
			f = open("pages/files/member_free.CSV", 'a', newline='')
			f_ = open("pages/files/member_free.CSV", 'r')
			read = csv.reader(f_)
			for row in read:
				st.write(row)
			wr = csv.writer(f)
			wr.writerow([name_student, phone_student, id, password, 3])
			f.close()
			#st.switch_page("pages/login_page.py")

signup()
