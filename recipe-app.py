import streamlit as st
import openai
import csv 
from PIL import Image

import os
os.environ['CURL_CA_BUNDLE'] = ''

openai.api_key = "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"

image = Image.open('images/banner.jpg')
st.image(image, use_column_width=True)

st.header("GPT-3 Recipe Ingredient Generator App")
review  = st.text_area("Enter Recipe Name")
button = st.button("Generate Ingredients")

#fine_tuned_model = openai.FineTune.retrieve(id='ft-QetNu29xNH4qH9ybPgM5pxfB').fine_tuned_model
fine_tuned_model = 'curie:ft-cognizant-2023-05-08-10-04-49'

def generate_reply(review,fine_tuned_model):
    response = openai.Completion.create(
    model = fine_tuned_model,
    prompt = f"Generate the ingredients for the given recipe: {review} ->",
    max_tokens=100,
    temperature=0.5
    )
    return response.choices[0].text


if button and review:
    with st.spinner("Generating Reply..."):
        reply = generate_reply(review,fine_tuned_model)
    st.write(reply)