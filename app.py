import streamlit as st
from utils.standaridzers import get_model_standaridzed
from utils.image_searcher import search_url
from utils.is_image import is_topic_image
from prompts import model_standaridzer, image_request_prompt

PATH_STANDARIDZER = "./data/catalogo_standarizador.csv"
PATH_CATALOG = "./data/products_catalog.csv"


def main():
    st.title("Simulacion de Standarizador")
    user_input = st.text_area("Conversación:")
    
    if st.button("Simular"):
        with_image = is_topic_image(user_input, image_request_prompt)

        if with_image:
            try:
                model_standarized = get_model_standaridzed(user_input, model_standaridzer,PATH_STANDARIDZER)
                url_image = search_url(model_standarized,PATH_CATALOG)
                st.write("Modelo estandarizado:", model_standarized)
                st.image(url_image, caption = model_standarized, use_column_width=True)
            except:
                st.write("Ups, no te entendí, puedes escribir nuevamente tu consulta?")
        else:
            st.write("El modelo que requieres es una gran alternativa, a continuacion te daré mas detalles.")
            
if __name__ == "__main__":
    main()