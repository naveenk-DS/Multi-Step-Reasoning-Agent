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

        if result["status"] == "success":
            st.success("Answer")
            st.write(f"**{result['answer']}**")
            st.caption(result["reasoning_visible_to_user"])

            with st.expander("Metadata"):
                st.json(result["metadata"])
        else:
            st.error("Failed")
            st.write(result["reasoning_visible_to_user"])
    else:
        st.warning("Please enter a question.")
