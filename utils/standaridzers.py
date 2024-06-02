import json
import openai
import streamlit as st
import os 
import csv

openai.api_key = st.secrets["OPENAI_API_KEY"]
PATH_STANDARIDZER = "./data/catalogo_standarizador.csv"

def get_model_standaridzed(message, system_prompt, path_to_file):

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt.format(convert_csv_to_string(path_to_file))},
            {"role": "user", "content": message}
            ]
            )
    strandized_model = response['choices'][0]['message']['content']
    json_strandized_model = json.loads(strandized_model)

    return json_strandized_model.get("model_standardized").capitalize()

def convert_csv_to_string(file_path):
    result = []
    
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            model_name = row['model_name']
            variations = row['variations']
            variations_list = [f'{v.strip()}' for v in variations.split(',')]
            variations_string = ', '.join(variations_list)
            result.append(f'{variations_string} refers to "{model_name}"')
    
    return '\n'.join(result)