import streamlit as st
from PIL import Image



st.sidebar.header('Les Dott de Grenoble!')

def accueil():
    st.markdown('Velos, Trotinettes')
    st.sidebar.markdown('Les Dott de Grenoble!')
    st.image('gretrott.jpeg')
    

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Accueil": accueil,
    "Page 2": page2,
    "Page 3": page3,
    }

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


