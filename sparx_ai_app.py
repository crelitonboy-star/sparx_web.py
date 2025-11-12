import streamlit as st
import openai

# ---- STREAMLIT PAGE CONFIG ----
st.set_page_config(page_title="⚡ Sparx AI", page_icon="⚡", layout="centered")

st.title("⚡ Sparx AI")
st.write("Your personal AI assistant powered by GPT-4.")

# ---- OPENAI API KEY ----
# In Streamlit Cloud: Add a secret called OPENAI_API_KEY
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ---- USER INPUT ----
user_input = st.text_input("You:", "")

# ---- CHAT FUNCTION ----
def chat_with_sparx(message):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Sparx AI, a friendly, witty, and helpful AI assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

# ---- SEND BUTTON ----
if st.button("Send") and user_input:
    reply = chat_with_sparx(user_input)
    st.markdown(f"**Sparx AI:** {reply}")
