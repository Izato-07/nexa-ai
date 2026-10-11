
import streamlit as st
from groq import Groq, APIError

st.set_page_config(
    page_title="Nexa AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Nexa AI")
st.caption("Your personal AI assistant")

try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    api_key = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Settings")

    system_prompt = st.text_area(
        "Custom instructions",
        value="You are Nexa AI, a helpful and concise assistant.",
        height=120,
        key="system_instructions"
    )

    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()

st.caption("Powered by Groq")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Message Nexa AI...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    if not api_key:
        st.error("Groq API key is missing. Add it in Streamlit Secrets.")
    else:
        with st.chat_message("assistant"):
            with st.spinner("Nexa AI is thinking..."):
                try:
                    client = Groq(api_key=api_key)

                    response = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=[
                            {
                                "role": "system",
                                "content": system_prompt
                            },
                            *st.session_state.messages[-12:]
                        ],
                        max_tokens=700
                    )

                    answer = (
                        response.choices[0].message.content
                        or "The model returned an empty response."
                    )

                    st.markdown(answer)
                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                except APIError as exc:
                    st.error(f"Groq API error: {exc}")
                except Exception as exc:
                    st.error(f"Something went wrong: {exc}")
