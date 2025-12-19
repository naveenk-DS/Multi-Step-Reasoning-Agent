import streamlit as st
from agent.agent import solve

st.set_page_config(
    page_title="Multi-Step Reasoning Agent",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Multi-Step Reasoning Agent")
st.caption("Planner → Executor → Verifier (Self-Checking)")

# Chat-style input
question = st.text_input(
    "Ask a math or logic question...",
    placeholder="Alice has 3 red apples and twice as many green apples as red. How many apples does she have?"
)

if st.button("▶ Run Agent"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    # ---- USER MESSAGE ----
    st.markdown("### 🧑 User")
    st.info(question)

    # ---- AGENT STATUS ----
    st.markdown("### 🤖 Agent is working...")
    with st.spinner("Thinking..."):

        # Call backend
        result = solve(question)

    # ---- PLANNER ----
    st.markdown("### 🧠 Planner")
    st.success("Plan created")

    if "plan" in result.get("metadata", {}):
        st.markdown("**Step-by-step plan:**")
        for i, step in enumerate(result["metadata"]["plan"], 1):
            st.write(f"{i}. {step}")

    # ---- EXECUTOR ----
    st.markdown("### ⚙️ Executor")
    st.info("Executing plan and computing result...")

    # ---- FINAL ANSWER ----
    st.markdown("### ✅ Final Answer")
    st.success(result["answer"])

    st.caption(result["reasoning_visible_to_user"])

