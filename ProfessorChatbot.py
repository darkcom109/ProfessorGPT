import streamlit as st
from openai import OpenAI

user = OpenAI(api_key="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")

st.title("ProfessorGPT App")
st.divider()
prompt = st.text_input("What do you want to learn?")
gptbutton = st.button("Teach Me")
st.caption("ProfessorGPT will work when you press the button.")
st.divider()

def generate_response():
    if gptbutton:
        with st.spinner("I am preparing your lecture"):
            response = user.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = [{"role": "user", "content": "Teach me the following concept: " + prompt}]
            )
        st.snow()
        st.write(response.choices[0].message.content)

if __name__ == "__main__":
    generate_response()