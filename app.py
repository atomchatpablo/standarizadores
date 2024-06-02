import streamlit as st
from utils.standaridzers import get_model_standaridzed
from utils.image_searcher import search_url
from prompts import model_standaridzer

PATH_STANDARIDZER = "./data/catalogo_standarizador.csv"
PATH_CATALOG = "./data/products_catalog.csv"


def main():
    st.title("Simulacion de Standarizador")
    user_input = st.text_area("Conversación:")
    
    if st.button("Simular"):
        model_standarized = get_model_standaridzed(user_input, model_standaridzer,PATH_STANDARIDZER)
        url_image = search_url(model_standarized,PATH_CATALOG)
        st.write("Modelo estandarizado:", model_standarized)
        st.image(url_image, caption = model_standarized, use_column_width=True)
    
if __name__ == "__main__":
    main()