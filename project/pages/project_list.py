import streamlit as st

def app():
    st.header(' 프로젝트 LIST ')
    
    st.markdown('''
                #### - 과제 1-1 : 프로젝트 환경 구축 절차 작성
                #### - 과제 1-2 : streamlit 라이브러리 분석
                #### - 과제 1-3 : api, 웹 스크래핑(크롤링), 공공데이터를 이용하여 자료 수집
                
                #### - 과제 2-1 : 시계열 자료(기상, 분자료/시간자료) 수집
                #### - 과제 2-2 : 시계열 자료 QC : 물리한계, 단계, 결측, 지속성 검사
                #### - 과제 2-3 : 시계열 자료 분석 (월평균/일평균 산출, 결측 자료 복구, 예측(가능할 경우), 그래프/표)
                ''')