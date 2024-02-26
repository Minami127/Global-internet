import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app


def main():
    st.title('전세계 인터넷 사용자수 통계')

    menu=['Home','EDA']

    choice = st.sidebar.selectbox('메뉴선택', menu)

    if choice == menu[0] :
        run_home_app()
    elif choice == menu[1] :
        run_eda_app()
    

    


if __name__ == '__main__':
    main()