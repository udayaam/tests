import os
import streamlit as st
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)

#Always return a response in JSON format. No additonal response should be there apart from JSON. JSON should have Review, Score, Suggestions, Good, & Bad fields. 

def model_call_critic(prompt, job_role):

    sys_prompt = "You are a medical expert. You need to give answer to the following question only and only from the document attached. The question is as follows: "+job_role
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": sys_prompt,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        model = "llama3-70b-8192"
    )

    return chat_completion.choices[0].message.content
