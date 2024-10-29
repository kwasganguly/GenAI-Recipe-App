import streamlit as st
import openai
openai.api_key = st.secrets['OPENAI_API_KEY']

st.header("GPT-3 Restaurant Review Replier")
review  = st.text_area("Enter Customer Review")
button = st.button("Generate Reply")

def generate_reply(review):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"This is a restaurant review replier bot. This restaurant has been launched recently and there might be instances where customers might come up with bad reviews and express disappointment. You have to understand customer sentiment and assure him to provide best services during next visit. If the customer has any concerns address them.Also let him know the address of any one of the offices in Kolkata so that he could get his query resolved if needed.\n\nReview:{review}\n\nreplay:",
    temperature=0.9,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    #st.write(response)
    return response.choices[0].text

if button and review:
    with st.spinner("Generating Reply..."):
        reply = generate_reply(review)
    st.write(reply)