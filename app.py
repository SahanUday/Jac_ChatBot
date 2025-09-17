import streamlit as st
import requests

API_URL = "http://localhost:8000/walker/Supervisor"

st.set_page_config(page_title="Jac ChatBot", page_icon="🤖")

st.title("🤖 Jac ChatBot")
st.write("Ask me anything about Jaseci and Walkers!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your question..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Reserve a spot for bot reply
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("💭 Thinking...")  # temporary message

        try:
            response = requests.post(
                API_URL,
                headers={"Content-Type": "application/json"},
                json={"query": prompt},  # ✅ correct request body
                timeout=60
            )
            response.raise_for_status()
            data = response.json()

            # Extract chatbot reply
            if "reports" in data and len(data["reports"]) > 0:
                bot_reply = data["reports"][0].get("ChatBot", "⚠️ No reply from server")
            else:
                bot_reply = "⚠️ Unexpected response format."

        except Exception as e:
            bot_reply = f"❌ Error: {e}"

        # Replace placeholder with final reply
        placeholder.markdown(bot_reply)

    # Save reply to history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
