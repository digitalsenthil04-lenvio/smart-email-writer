import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# --------------------------------------------------
# Streamlit Page
# --------------------------------------------------
st.set_page_config(page_title="Smart Email Writer", page_icon="📧")
st.title("📧 Smart Email Writer")

st.write("Generate professional emails instantly using AI.")

# --------------------------------------------------
# Validate API Key
# --------------------------------------------------
if not api_key:
    st.error("OPENAI_API_KEY not found. Please check your .env file.")
    st.stop()

# --------------------------------------------------
# LLM
# --------------------------------------------------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=api_key
)

# --------------------------------------------------
# Prompt Template
# --------------------------------------------------
template = """
You are a professional email writing assistant.

Write an email using the details below.

Recipient: {recipient}
Subject: {subject}
Purpose: {purpose}
Tone: {tone}

Return only the final email.
"""

prompt = PromptTemplate(
    input_variables=["recipient", "subject", "purpose", "tone"],
    template=template
)

# --------------------------------------------------
# Inputs
# --------------------------------------------------
recipient = st.text_input("Recipient Name / Role")
subject = st.text_input("Email Subject")
purpose = st.text_area("Purpose of the Email")

tone = st.selectbox(
    "Select Tone",
    ["Professional", "Friendly", "Apologetic", "Request", "Follow-up"]
)

# --------------------------------------------------
# Generate Button
# --------------------------------------------------
if st.button("Generate Email"):
    if not recipient or not subject or not purpose:
        st.warning("Please fill all fields.")
    else:
        with st.spinner("Writing your email..."):
            final_prompt = prompt.format(
                recipient=recipient,
                subject=subject,
                purpose=purpose,
                tone=tone
            )

            try:
                response = llm.invoke(final_prompt)
                st.subheader("Generated Email:")
                st.write(response.content)

            except Exception as e:
                st.error(f"Error: {e}")
