# __import__('pysqlite3')
# import sys
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import rag_main



# Set page configuration
st.set_page_config(page_title="RAG Template", page_icon=":speech_balloon:")

# Create Vector Storage
rag_main.create_vector_db()

# Set title
st.title("<Chat Title>")
st.subheader("Simple RAG Template")

# Create a text area for user input
user_input = st.text_area("Ask!:", height=100, placeholder="Placeholder...")

# Add a submit button
if st.button("Send"):
    if user_input.strip() != "":  
      with st.spinner("Thinking..."):
        response = rag_main.answer_question(user_input)
      # Display the user's message
      st.write(f"AI: {response}")

st.markdown(
    """
    ---
    <div style="text-align: center; font-size: 0.8em;">
        Developed by Pablo Menor🖥️

    </div>
    """,
    unsafe_allow_html=True
)