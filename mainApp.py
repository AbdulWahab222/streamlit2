import streamlit as st
from langchain.llms import OpenAI

st.title('Personal Learning Assistant 🎓')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text, detail_level="overview"):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    if detail_level == "overview":
        return str(llm(f"Provide a concise overview of {input_text}"))
    elif detail_level == "deep_dive":
        return str(llm(f"Explain {input_text} in detail"))
    else:
        return str(llm(f"Recommended resources for learning about {input_text}"))

with st.form('learning_form'):
    topic = st.text_input('Enter a topic you want to learn about:')
    detail_selection = st.radio("Select detail level", ["overview", "deep_dive", "resources"])
    submitted = st.form_submit_button('Learn')
    
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!')
    if submitted and openai_api_key.startswith('sk-'):
        response = generate_response(topic, detail_selection)
        st.info(response)
