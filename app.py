
import streamlit as st
import ollama

st.set_page_config(
    page_title="Nexa AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Nexa AI")
st.caption("Your personal AI assistant · Local mode")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Settings")

    model = st.selectbox(
        "AI Model",
        ["qwen2.5:3b"],
        key="model_selector"
    )

    system_prompt = st.text_area(
        "Custom instructions",
        value="You are Nexa AI, a helpful and concise assistant.",
        height=120,
        key="system_instructions"
    )

    if st.button("Clear conversation", key="clear_chat"):
        st.session_state.messages = []
        st.rerun()

st.caption("Runs locally on your computer. No OpenAI API key required.")

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

    with st.chat_message("assistant"):
        with st.spinner("Nexa AI is thinking..."):
            try:
                history = st.session_state.messages[-12:]

                response = ollama.chat(
                    model=model,
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt
                        },
                        *history
                    ]
                )

                answer = response["message"]["content"]
                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as exc:
                st.error(
                    "Could not connect to Ollama. Make sure Ollama "
                    "is running and qwen2.5:3b is installed."
                )
                st.caption(f"Technical details: {exc}")
