import json
import openai
import streamlit as st
import os 
import csv

openai.api_key = st.secrets["OPENAI_API_KEY"]
PATH_STANDARIDZER = "./data/catalogo_standarizador.csv"

def is_topic_image(message, system_prompt):

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
            ]
            )
    is_image = response['choices'][0]['message']['content']
    json_response = json.loads(is_image)

    return json_response.get("response")