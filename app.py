import streamlit as st
from agent.agent import solve

st.set_page_config(
    page_title="Multi-Step Reasoning Agent",
    page_icon="🧠"
)

st.title("🧠 Multi-Step Reasoning Agent")

question = st.text_area(
    "Enter your question:",
    placeholder="A movie starts at 23:40 and ends at 01:10. How long is it?"
)

if st.button("Solve"):
    if question.strip():
        with st.spinner("Thinking..."):
            result = solve(question)

        # ✅ SHOW ONLY REQUIRED FIELDS
        st.json({
            "answer": result["answer"],
            "status": result["status"],
            "reasoning_visible_to_user": result["reasoning_visible_to_user"]
        })

    else:
        st.warning("Please enter a question.")
