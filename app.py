import streamlit as st

st.set_page_config(page_title="Мій Супер-Додаток", page_icon="https://img.icons8.com/nolan/1200/bongo-cat.jpg")

st.title("Nice to meet you on my webapp")

tab1, tab2 = st.tabs(["About me", "My tool"])

with tab1:
    st.header("Знайомство з автором")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("Toad_Frog_Aniimated_v1_1000_0001.jpg", width=400)
    with col2:
        st.subheader("Привіт, я майбутній Python Developer!")
        st.write("Я навчаюсь в Малій Комп'ютерній Академії IT STEP. Створюю круті веб-додатки та вивчаю Streamlit")
    
    with st.container():
        st.info("Контакти для зв`язку")
        st.markdown("- GitHub: [Мій профіль](https://github.com)")
        st.markdown("- E-Mail: andreww@itstep.org")

with tab2:
    st.header("Мій інструмент")
    st.info("У процессі розробки")